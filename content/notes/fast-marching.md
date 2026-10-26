---
source: report/notes/fast-marching.md
date: ''
kind: note
comments: true
generated: 2026-10-26T20:52:49
---

# Fast marching method

<p class="doc-meta"><span class="chip chip-note">Note</span></p>

---

## 1. Executive Summary & Problem Context

In spatial modeling and urban form analysis, converting point or footprint-based parcel representations into realistic influence zones often leads to geometrical degeneracies when using classical Voronoi tessellations:
- **Submerged Sites:** Sites with small weights are completely absorbed by sites with large weights.
- **Site Eviction:** Points are pushed outside their own Voronoi cells.
- **Topological Leakage / Over-reaching:** Unconstrained Euclidean expansion allows massive structures (e.g., shopping malls) to "wrap around" barriers and absorb parcels located behind intervening buildings.

The **Fast Marching Method (FMM)** resolves these pathologies by reformulating spatial allocation as a **boundary-value propagation problem** governed by the **Eikonal partial differential equation**. Building footprints serve as zero-cost initialization interfaces, opposing footprints act as impenetrable obstacles, and the Total Floor Area (TFA) parameterizes the local propagation speed.

---

## 2. Continuous Mathematical Formulation

### 2.1 The Eikonal Equation

The evolution of an advancing monotonically moving interface through an $n$-dimensional domain $\Omega \subset \mathbb{R}^n$ can be characterized by an arrival time function $T(x)$, which describes the exact time at which the expanding wavefront crosses position $x \in \Omega$.

The governing boundary-value problem is the stationary **Eikonal Equation**:


$$|\nabla T(x)| = \frac{1}{F(x)}, \quad x \in \Omega \setminus \Gamma$$



$$\text{subject to} \quad T(x) = 0, \quad x \in \Gamma$$


where:
- $T(x): \Omega \to [0, \infty)$ denotes the arrival time (or geodesic action potential).
- $\nabla T(x) = \left( \frac{\partial T}{\partial x_1}, \dots, \frac{\partial T}{\partial x_n} \right)$ is the spatial gradient vector of the arrival time.
- $F(x) > 0$ is the scalar speed function of the front at point $x$.
- $f(x) = \frac{1}{F(x)}$ is the slowness or cost function.
- $\Gamma = \bigcup_{i=1}^M \Gamma_i$ represents the initial source boundary consisting of $M$ discrete interfaces (e.g., building footprint boundaries).

### 2.2 Geodesic Metric and Characteristics

By the method of characteristics and the calculus of variations (Fermat's Principle), the solution $T(x)$ to the Eikonal equation corresponds to the minimum travel-time metric:


$$T(x) = \inf_{\gamma \in \mathcal{P}(\Gamma, x)} \int_0^L \frac{1}{F(\gamma(s))} \, ds$$


where $\mathcal{P}(\Gamma, x)$ is the collection of all rectifiable paths $\gamma(s)$ parameterized by arc length $s \in [0, L]$ starting at any point on the boundary $\Gamma$ and terminating at $x$.

The characteristics (orthogonal trajectories of the level sets $\{x \mid T(x) = c\}$) satisfy:


$$\frac{d x(s)}{ds} = F(x) \frac{\nabla T(x)}{|\nabla T(x)|}$$


Because $F(x) > 0$, the arrival time function $T(x)$ is strictly non-decreasing along trajectories, precluding characteristics from turning backward.

---

## 3. Discretization and Numerical Schemes

Direct central differences applied to $|\nabla T| = 1/F$ produce numerical instabilities and fail to satisfy entropy conditions at shock formations (where wave fronts collide). A correct viscosity solution must employ an **upwind finite difference scheme** that respects the domain of dependence.

### 3.1 Upwind Finite Difference Operator in $\mathbb{R}^2$

Consider a regular Cartesian grid with spacing $\Delta x$ and $\Delta y$. Let $T_{i,j} \approx T(i\Delta x, j\Delta y)$. 

The Rouy-Tourin / Sethian first-order upwind discretization of $|\nabla T|^2 = \frac{1}{F^2}$ is formulated as:


$$\left[ \max\left( D_{ij}^{-x} T, -D_{ij}^{+x} T, 0 \right) \right]^2 + \left[ \max\left( D_{ij}^{-y} T, -D_{ij}^{+y} T, 0 \right) \right]^2 = \frac{1}{F_{ij}^2}$$


where the standard forward and backward difference operators are defined as:


$$D_{ij}^{-x} T = \frac{T_{i,j} - T_{i-1,j}}{\Delta x}, \quad D_{ij}^{+x} T = \frac{T_{i+1,j} - T_{i,j}}{\Delta x}$$



$$D_{ij}^{-y} T = \frac{T_{i,j} - T_{i,j-1}}{\Delta y}, \quad D_{ij}^{+y} T = \frac{T_{i,j+1} - T_{i,j}}{\Delta y}$$


### 3.2 Quadratic Formulation for Grid Updates

For isotropic cells ($\Delta x = \Delta y = h$), define the minimum upstream values along each axis:


$$T_x = \min(T_{i-1,j}, T_{i+1,j})$$



$$T_y = \min(T_{i,j-1}, T_{i,j+1})$$


Assume without loss of generality that $T_x \le T_y$. The update equation simplifies to the algebraic quadratic form:


$$(T - T_x)^2 + (T - T_y)^2 = \frac{h^2}{F_{ij}^2}$$


Expanding gives:


$$2T^2 - 2(T_x + T_y)T + (T_x^2 + T_y^2) - \frac{h^2}{F_{ij}^2} = 0$$


Solving for $T$ via the quadratic formula yields:


$$T = \frac{T_x + T_y + \sqrt{(T_x + T_y)^2 - 2\left( T_x^2 + T_y^2 - \frac{h^2}{F_{ij}^2} \right)}}{2} = \frac{T_x + T_y + \sqrt{2\frac{h^2}{F_{ij}^2} - (T_x - T_y)^2}}{2}$$


#### Validity Condition (Dimensional Degeneracy Check)
The two-dimensional characteristic wave reaches $(i,j)$ simultaneously from both axes if and only if the discriminant is strictly non-negative and $T > T_y$:


$$|T_x - T_y| < \frac{h}{F_{ij}}$$


If this condition fails ($T_y - T_x \ge \frac{h}{F_{ij}}$), information propagates strictly along the 1D direction from $T_x$, collapsing the update to:


$$T = T_x + \frac{h}{F_{ij}}$$


---

## 4. Algorithmic Architecture

The Fast Marching Method mimics Dijkstra's shortest-path algorithm over a continuous grid. The mesh nodes $\mathcal{N}$ are partitioned into three mutually exclusive sets:

1. **$\mathcal{K}$ (Known / Frozen):** Nodes where the exact arrival time $T$ has been computed and fixed.
2. **$\mathcal{T}$ (Trial / Narrow Band):** Immediate neighbors of $\mathcal{K}$ whose provisional values have been computed; tracked inside a min-priority heap.
3. **$\mathcal{F}$ (Far / Unvisited):** Nodes that have not yet been evaluated ($T = \infty$).

```
[  F A R  ]  --->  [ T R I A L (Heap) ]  --->  [ K N O W N ]
T = Infinity        Monitored Candidates        Frozen Values
```

### 4.1 Algorithmic Procedure

```text
Algorithm: Multi-Label Fast Marching with Obstacle Constraints
-------------------------------------------------------------------------
Input:  - Domain Grid of size N x M with spacing h
        - Seed Footprints: S_k for each building k in {1, ..., K}
        - Propagation Speeds: F_k (derived from TFA)
        - Boundary Blocks / Parcel Mask: B_mask
Output: - Arrival Time Field T(x, y)
        - Label Allocation Field L(x, y)

1. Initialization:
   For every grid node (i, j):
       If (i, j) in S_k (inside footprint of building k):
           T[i, j] = 0.0
           L[i, j] = k
           State[i, j] = KNOWN
       Else if (i, j) outside parcel boundary B_mask:
           T[i, j] = Infinity
           L[i, j] = -1
           State[i, j] = OBSTACLE
       Else:
           T[i, j] = Infinity
           L[i, j] = 0
           State[i, j] = FAR

2. Populate Narrow Band (Trial):
   Initialize Min-Priority Heap Q
   For each node (i, j) in KNOWN:
       For each orthogonal neighbor (ni, nj) in 4-neighborhood of (i, j):
           If State[ni, nj] == FAR:
               Compute T_trial using Quadratic Update with F = F[L[i, j]]
               T[ni, nj] = T_trial
               L[ni, nj] = L[i, j]
               State[ni, nj] = TRIAL
               Insert (ni, nj, T_trial) into Q

3. Marching Loop:
   While Q is not empty:
       Pop (ci, cj) with minimal T from Q
       State[ci, cj] = KNOWN
       
       For each orthogonal neighbor (ni, nj) of (ci, cj):
           If State[ni, nj] == OBSTACLE or State[ni, nj] == KNOWN:
               Continue
           
           parent_label = L[ci, cj]
           local_speed  = F[parent_label]
           T_candidate  = SolveQuadraticEikonal(ni, nj, local_speed)
           
           If State[ni, nj] == FAR:
               T[ni, nj] = T_candidate
               L[ni, nj] = parent_label
               State[ni, nj] = TRIAL
               Insert (ni, nj, T_candidate) into Q
           Else if State[ni, nj] == TRIAL:
               If T_candidate < T[ni, nj]:
                   T[ni, nj] = T_candidate
                   L[ni, nj] = parent_label
                   DecreaseKey((ni, nj), T_candidate) in Q

4. Return Fields T and L.
```

### 4.2 Computational Complexity

For a grid containing $N$ total elements:
- Each node enters and exits the `TRIAL` heap at most once.
- Inserting and deleting minimum elements from a binary min-heap requires $\mathcal{O}(\log |\mathcal{T}|)$ operations.
- Since $|\mathcal{T}| \le N$, total algorithmic time complexity is:


$$\mathcal{O}(N \log N)$$


Using advanced priority structures (e.g., untidy priority queues or Fibonacci heaps) can theoretically lower the amortized complexity toward $\mathcal{O}(N)$, though standard binary heaps remain optimal in practical spatial memory layouts.

---

## 5. Overcoming Voronoi Pathologies in Urban Blocks

### 5.1 Prevention of Submerged Sites
In conventional Voronoi configurations, if building $A$ has weight $w_A \gg w_B$, the condition $\|x - p_B\| - w_B > \|x - p_A\| - w_A$ can hold over the entirety of $\Omega$, leaving site $B$ with no cell ($\emptyset$). 

In the FMM framework:
- Footprint $B$ is explicitly seeded at initialization: $\forall x \in \text{Footprint}_B \implies T(x) = 0$.
- By causality of the upwind scheme, $T(x) \ge 0$ everywhere.
- Consequently, site $B$ retains its base footprint area:


$$\text{Area}(\text{Cell}_B) \ge \text{Area}(\text{Footprint}_B) > 0$$


### 5.2 Prevention of Site Eviction
Because every building centroid $p_i$ is embedded within $\text{Footprint}_i$, and that footprint is initialized with $L(x) = i$, the point $p_i$ is geometrically guaranteed to reside within its assigned allocation zone:


$$p_i \in \text{Footprint}_i \subseteq \text{Cell}_i$$


### 5.3 Immunity to Topological Leakage (Wrapping Effect)
Consider an irregular triangular block with three adjacent buildings along one edge: a large mall ($M$), a medium house ($H_1$), and a small house ($H_2$).

```
                      / \
                     /   \
                    /     \   <-- Open triangular interior
                   /       \
                  /  [H2]   \
                 /   [H1]    \
                /____[M]______\
```

- **In Euclidean Voronoi:** The high weight of $M$ projects radially outwards. The metric circle/hyperbola of $M$ expands through the empty interior, wrapping around $H_1$ and $H_2$ to seize the vacant space directly behind $H_2$.
- **In Obstacle-Constrained FMM:**
  1. The footprints of $H_1$ and $H_2$ are impenetrable barriers.
  2. Any characteristic ray originating from $M$ attempting to reach the space behind $H_2$ must curve around the obstacle chain, satisfying the geodesic boundary condition:


$$L_{\text{geodesic}}(M \to \text{Behind } H_2) \gg L_{\text{geodesic}}(H_2 \to \text{Behind } H_2)$$


  3. Even if $F_M \gg F_{H_2}$, the travel time $T(x) = \int \frac{1}{F} ds$ for $H_2$ over an infinitesimal distance directly adjacent to its back wall is near zero ($T \approx \epsilon$), whereas the mall's wave front must traverse the physical perimeter distance. $H_2$ naturally captures its immediate contextual surroundings.

---

## 6. Implementation Notes: Parameterizing Speed from TFA

To map **Total Floor Area (TFA)** to the continuous propagation speed $F_k$, avoid simple linear mappings if weight disparities span multiple orders of magnitude.

### 6.1 Recommended Speed Scaling Formulations

Let $\text{TFA}_k$ be the total floor area of building $k$, and let $A_{\text{fp}, k}$ be the base footprint ground area.

1. **Sub-linear / Square-Root Scaling (Recommended):**
   Ground allocation grows in two dimensions ($L \propto \sqrt{\text{Area}}$). Map speed to equivalent linear expansion:


$$F_k = F_{\text{base}} \cdot \left( \frac{\text{TFA}_k}{\overline{\text{TFA}}} \right)^{1/2}$$


2. **Logarithmic Scaling (For Extreme Density Disparities):**
   When high-rise towers ($\text{TFA} \sim 100{,}000\text{ m}^2$) neighbor single-story structures ($\text{TFA} \sim 100\text{ m}^2$):


$$F_k = F_{\text{base}} \cdot \left( 1 + \alpha \ln\left( 1 + \frac{\text{TFA}_k}{A_{\text{fp}, k}} \right) \right)$$


### 6.2 Target Area Termination Condition
If each building has an upper bound quota $A_k^{\max}$, augment step 3 of the Marching Loop:
- Maintain an active counter of allocated cells $C_k = \sum \mathbb{I}(L = k)$.
- Once $C_k \ge \frac{A_k^{\max}}{h^2}$, freeze expansion for label $k$ by setting $F_k \to 0$.
- Remaining unallocated space is dynamically absorbed by neighboring active fronts.
