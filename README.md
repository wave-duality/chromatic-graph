# Chromatic-Graph
A _proper vertex coloring_ of a graph is an assignment function $f: v(G) \to C$ for some colors $C$. This project computes a closed form for the number of ways to color the vertices of a given graph $G$ with $k$ colors such that adjacent vertices are distinct colors.

## Introduction, Background, and Motivation
The problem of assigning colors to vertices on a graph such that adjacent vertices (connected via an edge) have a different color has various applications; for instance, consider the puzzle Sudoku, which is easily represented as a graph coloring problem, or a more complex algorithm like assigning class periods to students.

A natural question to ask is, for a given graph $G,$ how many colors $k$ do we need such that this coloring can be achieved? It turns out that this is a relatively easy problem, in the sense that there is a deterministic and recursive algorithm that can compute this for any graph (albeit slowly), and we denote this minimal number of colors by $\chi(G),$ the _chromatic number_ of graph $G.$ 

A second question to ask is, if we have $k$ colors, where $k \geq \chi(G),$ how many _ways_ can we color the graph $G$ such that the adjacent vertex condition is upheld? To answer this question, we need a little machinery.

## Chromatic Polynomials
Define the chromatic polynomial to be a function $\lambda: (G, \mathbb{Z}^{\geq \chi(G)}) \to \mathbb{Z})$ such that $\lambda(G, t)$ is the number of ways to color $G$ with $t$ colors. It's unclear at first why such a polynomial must even exist, but we can recursively find $\lambda$ as follows: for any edge $e \in e(G),$ it holds that $\lambda(G, t) = \lambda(G-e, t) - \lambda(G/e, t)$ (to prove, consider $p$ and $q$ connected by $e.$ When is a coloring of $G-e$ not a coloring of $G$?), where $G-e$ is the graph $G$ with edge $e$ simply _deleted_ and $G/e$ is the graph $G$ with edge $e$ _contracted_.

Since we can easily evaluate $\lambda(G, t)$ when $G$ has 0 or 1 edges (for instance, $\lambda(G, t) = t^{v(G)}$ if $|e(G)| = 0$), the recursion successfully outputs a polynomial for any graph $G.$ Also, it makes sense that $\lambda(G, t)$ evaluates to $0$ for $t < \chi(G),$ so a cool corollary is that the integers $0, \cdots, \chi(G)-1$ are all necessarily roots of $\lambda(G, t)!$

## Code
The primary purpose of the code is to implement the chromatic recurrence (detailed above), along with some helpful functions that draw the graphs (by using roots of unity as points), generate random graphs, etc. 

With this, you can figure out how many ways there are to color any graph $G$ with $k$ colors such that adjacent vertices have different colors!

## Optimization
This code can be easily optimized (by a lot) by choosing a suitable $e$ instead of a random $e$ during the recursive step; this requires calculating the minimum of $e(G/e')$ over $e' \in e(G),$ which is not a difficult task. This task is #P-complete, and this algorithm (when optimized) runs in $\mathcal{O}(\phi^{v(G) + e(G)}).$


