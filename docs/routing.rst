.. _routing:

Routing problems
********************************************************************************

.. todo::
   Adapt everything: figures, maths, ...

.. index::
   single: routing problems

In this chapter we will consider several problems related to routing, discussing and characterizing different mathematical optimization formulations.  The roadmap is the following.
Section :ref:`tsp` presents several mathematical formulations for the traveling salesman problem (TSP), one of the most extensively studied optimization problems in operations research.
In section :ref:`tsptw` we extend one of the formulations for the TSP for dealing with the case where there is a time interval within which each vertex must be visited.
Section :ref:`cvrp` describes the capacity-constrained delivery planning problem, showing a solution based on the cutting plane method.

   

.. _tsp:

Traveling Salesman Problem
==========================

.. index:: traveling salesman problem
.. index:: TSP

Here we consider the traveling salesman problem, which is a typical example of a combinatorial optimization problem in routing.
Let us start with an example of the traveling salesman problem.


.. case study
.. compound::

   You are thinking about taking a vacation and taking a tour of Europe.  You are currently in Zurich, Switzerland, and your aim is to watch a bullfight in Madrid, Spain, to see the Big Ben in London, U.K., to visit the Colosseum in Rome, Italy, and to drink authentic beers in Berlin, Germany.  You decide to borrow a rental helicopter, but you have to pay a high rental fee proportional to the distance traveled.  Therefore, after leaving, you wish to return to Zurich again, after visiting the other four cities (Madrid, London, Rome, Berlin) by traveling a distance as short as possible. Checking the travel distance between cities, you found that it is as shown in Figure :ref:`fig-tsp`.  Now, in what order should you travel so that distance is minimized?

   .. _fig-tsp:

   .. figure:: FIGS/tsp.png
      :scale: 10 %
      :align: center

      Traveling salesman problem

      Graph representation of cities in Europe (numerical value on edirs is the distance in miles) and optimum solution (thick line).


Let us define the problem without ambiguity.  This definition is based on the concept of graph, introduced in Section :ref:`graph`.

.. definition
.. pull-quote::
   Traveling salesman problem (TSP)

   Given an undirected graph :math:`G = (V, E)` consisting of :math:`n` vertices (cities), a function :math:`c: E \to \mathbb{R}` associating a distance (weight, cost, travel time) to each edge, find a tour which passes exactly once in each city and minimizes the total distance (i.e., the length of the tour).

   
When the problem is defined on a non-oriented graph (called an *undirected graph*), as in the above example, we call it a *symmetric traveling salesman problem*.  Symmetric means that the distance from a given point :math:`a` to another point :math:`b` is the same as the distance from :math:`b` to :math:`a`.  Also, the problem defined on a graph with orientation  (called a *directed graph* or *digraph*)) is called an asymmetric traveling salesman problem; in this case, the distance for going from a point to another may be different of the returning distance.  Of course, since the symmetric traveling salesman problem is a special form of the asymmetric case, a formulation for the latter can be applied as it is to symmetric problems (independently from whether it can be solved efficiently or not).

In this section we will see several formulations for the traveling salesman problem (symmetric and asymmetric) and compare them experimentally.  Section :ref:`tsp-dfj` presents the subtour elimination formulation for the symmetric problem proposed by Dantzig-Fulkerson-Johnson :cite:`Dantzig1954`.   
Section :ref:`tsp-mtz` presents an enhanced formulation based on the notion of *potential* for the asymmetric traveling salesman problem proposed by Miller-Tucker-Zemlin :cite:`Miller1969`.
Sections :ref:`tsp-scf` and :ref:`tsp-mcf` propose formulations using the concept of flow in a graph.
In :ref:`tsp-scf` we present a single-commodity flow formulation, and in :ref:`tsp-mcf` we develop a multi-product flow formulation.


.. _tsp-dfj:

Subtour elimination formulation
---------------------------------------------

.. index:: TSP: subtour elimination formulation
.. index:: TSP: Dantzig-Fulkerson-Johnson formulation

There are several ways to formulate the traveling salesman problem.  We will start with a formulation for the symmetric case.
Let variables :math:`x_e` represent the edges selected for the tour, i.e., let :math:`x_e` be 1 when edge :math:`e \in E` is in the tour, 0 otherwise.

For a subset :math:`S` of vertices, we denote :math:`E(S)` as the set of edges whose endpoints are both included in :math:`S`, and :math:`\delta(S)` as the set of edges such that one of the endpoints is included in :math:`S` and the other is not.  In order to have a traveling route, the number of selected edges connected to each vertex must be two.  Besides, the salesman must pass through all the cities; this means that any tour which does not visit all the vertices in set :math:`V` must be prohibited.  One possibility for ensuring this is to require that for any proper subset :math:`S \subset V` with cardinality :math:`|S| \geq 2`, the number of selected edges whose endpoints are both in :math:`S` is, at most, equal to the number of vertices :math:`|S|` minus one.

From the above discussion, we can derive the following formulation.

.. math::
   & \mbox{minimize} \quad   & \sum_{e \in E} c_{e} x_{e}  &       \\
   & \mbox{subject to} \quad & \sum_{e \in \delta(\{i\})}  x_{e} = 2 \qquad & \forall i \in V,\\
   &                         & \sum_{e \in E(S)}  x_{e} \leq |S|-1   \qquad & \forall S \subset V, 2 \leq |S| \leq |V|-2,\\
   &                         & X_{e} \in \{0,1\}                            & \forall e \in E.

Since the number of edges connected to a vertex is called its degree, the first constraint is called *degree constraint*.
The second constraint is called the *subtour elimination inequality* because it excludes partial tours (i.e., cycles which pass through a proper subset of vertices, rather than passing through all of them).

.. index:: TSP: subtour elimination inequality
.. index:: TSP: cutset inequality

For a given subset :math:`S` of vertices, if we double both sides of the subtour elimination inequality and then subtract the degree constraint

.. math::
   \sum_{e \in \delta(\{i\})}  x_{e} = 2

for each vertex :math:`i \in S`, we obtain the following inequality:

.. math::
   \sum_{e \in \delta(S)}  x_{e} \geq 2, \qquad & \forall S \subset V, |S| \geq 2. \\

This constraint is called a *cutset inequality*, and in the case of the traveling salesman problem it has the same strength as the subtour elimination inequality.  In the remainder of this chapter, we consider only the cutset inequality.

The number of subsets of a set increases exponentially with the size of the set.
Similarly, the number of subtour elimination constraints (cutset constraints) for any moderate size instance is extremely large.  Therefore, we cannot afford solving the complete model; we have to resort to the so-called *cutting plane method*, where constraints are added as necessary.

.. index:: TSP: separation problem
.. index:: maximum flow problem
.. index:: minimum problem

Assuming that the solution of the linear relaxation of the problem using only a subset of constraints is :math:`\bar{x}`,
the problem of finding a constraint that is not satisfied for this solution is usually called the *separation problem* (notice that components of :math:`\bar{x}` can be fractional values, not necessarily 0 or 1).
In order to design a cutting plane method, it is necessary to have an efficient algorithm for the separation problem.
In the case of the symmetric traveling salesman problem, we can obtain a violated cutset constraint (a subtour elimination inequality) by solving a maximum flow problem for a network having :math:`\bar{x}_e` as the capacity, where :math:`\bar{x}_e` is the solution of the linear relaxation with a (possibly empty) subset of subtour elimination constraints.  Notice that if this solution has, e.g., two subtours, the maximum flow from any vertex in the first subtour to any vertex in the second is zero.  
By solving finding the maximum flow problem, we also obtain de solution of the *minimum cut problem*, i.e., a partition of the set of vertices :math:`V` into two subsets :math:`(S, V \setminus S)` such that the capacity of the edges between :math:`S` and :math:`V \setminus S` is minimal :cite:`Ford1956`.
A minimum cut is obtained by solving the following max-flow problem, for sink vertex :math:`k = 2, 3, \ldots, n`:

.. math::
   \mbox{maximize} \quad   & \sum_{j: j>1} f_{1j}  &      \\
   \mbox{subject to} \quad & \sum_{j: i<j}  f_{ij} - \sum_{j: i>j} f_{ji} = 0 \qquad & \forall i : i \neq 1, i \neq k  \\
                           & -\bar{x}_{ij} \leq f_{ij} \leq \bar{x}_{ij}      \qquad & \forall i < j

The objective represents the total flow out of node 1.
The first constraint concerns flow preservation at each vertex other than the source vertex 1 and the target vertex :math:`k`, and the second constraint limits flow capacity on each arc.
In this model, in order to solve a problem defined on an undirected graph into a directed graph, a negative flow represents a flow in the opposite direction.  

As we have seen, if the optimum value of this problem is less than 2, then a cutset constraint (eliminating a subtour) which is not satisfied by the solution of the previous relaxation has been found.  We can determine the corresponding cut :math:`(S, V \setminus S)` by setting :math:`S = \{ i \in V : \pi_i \neq 0 \}`,  where :math:`\pi` is the optimal dual variable for the flow conservation constraint.

.. index:: connected graph
.. index:: connected component

Here, instead of solving the maximum flow problem, we will use a convenient method to find *connected components* for the graph consisting of the edges for which :math:`x_e` is positive in the previous formulation, when relaxing part of the subtour elimitation constraints.  A graph is said to be *connected* if there is a path between any pair of its vertices.  A *connected component* is a maximal connected subgraph, i.e., a connected subgraph such that no other connected subgraph strictly contains it.  To decompose the graph into connected components, we use a Python module called `networkX` [#f1-routing]_.

The following function `addcut` takes as argument a set of edges, and can be used to add a subtour elimination constraint corresponding to a connected component :math:`S (\neq V)`.  

.. code-block:: python
   :linenos:

    def addcut(cut_edges):
        G = networkx.Graph()
        G.add_edges_from(cut_edges)
        Components = list(networkx.connected_components(G))
        if len(Components) == 1:
            return False
        model.freeTransform()
        for S in Components:
            model.addCons(quicksum(x[i,j] for i in S for j in S if j>i) <= len(S)-1)
        return True

In the second line of the above program, we create an empty undirected graph object :math:`G` by using the `networkx` module and construct the graph, by adding vertices and edges in the current solution `cut_edges`, in line 3.
Next, in line 4, connected components are found by using function `connected_components`.  If there is one connected component (meaning that there are no subtours), `False` is returned.  Otherwise, the subtour elimination constraint is added to the model (lines 7 to 10).

Using the `addcut` function created above, an algorithm implementing the cutting plane method for the symmetric travelling salesman problem is described as follows.

.. code-block:: python
   :linenos:

    def solve_tsp(V,c):
        model = Model("tsp")
        model.hideOutput()
        x = {}
        for i in V:
            for j in V:
                if j > i:
                    x[i,j] = model.addVar(ub=1, name="x(%s,%s)"%(i,j))
        for i in V:
            model.addCons(quicksum(x[j,i] for j in V if j < i) + \
                          quicksum(x[i,j] for j in V if j > i) == 2, "Degree(%s)"%i)
        model.setObjective(quicksum(c[i,j]*x[i,j] for i in V for j in V if j > i), "minimize")
        EPS = 1.e-6
        isMIP = False
        while True:
            model.optimize()
            edges = []
            for (i,j) in x:
                if model.getVal(x[i,j]) > EPS:
                    edges.append( (i,j) )
            if addcut(edges) == False:
                if isMIP:     # integer variables, components connected: solution found
                    break
                model.freeTransform()
                for (i,j) in x:     # all components connected, switch to integer model
                    model.chgVarType(x[i,j], "B")
                    isMIP = True
        return model.getObjVal(),edges

Firstly, the linear optimization relaxation of problem (without subtour elimination constraints) is constructed from lines 4 to 12.
Next, in the `while` iteration starting at line 15, the current model is solved and cut constraints are added until the number of connected components of the graph becomes one.
When there is only one connected component, variables are restricted to be binary (lines 25 and 26) and the subtour elimination iteration proceeds.
When there is only one connected component in the problem with integer variables, it means that the optimal solution has been obtained; therefore the iteration is terminated and the optimal solution is returned.

In the method described above, we used a method to re-solve the mixed integer optimization problem every time a subtour elimination constraint is added.  However, it is also possible to add these constraints during the execution of the branch-and-bound process.

!!!!!  How, in SCIP ?????
..
    but applying the branch and bound method by using the cbLazy function added in Gurobi 5.0

.. index::
   single: cutting plane method
   single: valid inequality
   single: cutting plane
   single: facet-defining

..
    !!!!! improve fig-cpI !!!!!
    

.. NOTE::

   **Margin seminar 6**

   *Cutting plane and branch-and-cut methods*

    The *cutting plane method* was originally applied to the traveling salesman problem by George Dantzig, one of the founders of linear optimization, and his colleagues Ray Fulkerson and Selmer Johnson, in 1954.  Here, let us explain it by taking as an example the maximum stable set problem, introduced in Section :ref:`mssp`.

    Let's consider a simple illustration consisting of three points (Figure :ref:`fig-cpI`, top).
    Binary variables :math:`x_1, x_2, x_3`, represented as a point in the three-dimensional space :math:`(x_1, x_2, x_3)`, indicate whether the corresponding vertices are in the maximum stable set or not.
    Using these variables, the stable set problem can be formulated as an integer optimization problem as follows.

    .. math::
       & \mbox{maximize} \quad   & x_1 + x_2 + x_3\\
       & \mbox{subject to} \quad & x_1 + x_2 \leq 1\\
       &                         & x_1 + x_3 \leq 1\\
       &                         & x_2 + x_3 \leq 1\\
       &                         & x_1, x_2, x_3 \in \{0,1\}

    The constraints in the above formulation state that both endpoints of an edge can not be placed in a stable set at the same time.  This instance has four feasible solutions: :math:`(0,0,0), (1,0,0), (0,1,0), (0,0,1)`.  The smallest space that "wraps around" those points is called a polytope; in this case, it is a tetrahedron, defined by these 4 points, and shown in the bottom-left image of Figure :ref:`fig-cpI`.  An optimal solution of the linear relaxation can be obtained by finding a vertex of the polyhedron that maximizes the objective function :math:`x_1 + x_2 + x_3`.  This example is obvious, and any of the points :math:`(1, 0, 0), (0, 1, 0), (0, 0, 1),` is an optimal solution, with optimum value 1.

    .. _fig-cpI:

    .. figure:: FIGS/CuttingPlaneI.png
       :scale: 25 %
       :align: center
       :alt: image 

       Polyhedra for the maximum stable set problem
       
       Maximum stable set instance (upper figure).  Representation of the feasible region as a polyhedron, based on its extreme points (lower-left figure).  The inequality system corresponding to its linear relaxation is is :math:`x_1 + x_2 \leq 1; x_1 + x_3 \leq 1; x_2 + x_3 ≤ 1; x_1, x_2, x_3 ≥ 0`; this space, and an optimum solution, are represented in the lower-right figure.

    In general, finding a linear inequality system to represent a polyhedron --- the so-called *convex envelope* of the feasible region --- is more difficult than solving the original problem, because all the vertices of that region have to be enumerated; this is usually intractable.  As a realistic approach, we will consider below a method of gradually approaching the convex envelope, starting from a region, containing it, defined by a linear inequality system.

    First, let us consider the linear optimization relaxation of the stable set problem, obtained from the formulation of the stable set problem by replacing the integrality constraint of each variable (:math:`x_i \in \{0,1\}`) by the constraints:
    
    .. math::
       0 \leq x_1 \leq 1,\\
       0 \leq x_2 \leq 1,\\
       0 \leq x_3 \leq 1.

    Solving this relaxed linear optimization problem (the *linear relaxation*) yields an optimum of 1.5, with optimal solution (0.5, 0.5, 0.5) (Figure :ref:`fig-cpI`, bottom-right figure).  In general, only solving the linear relaxation does not lead to an optimal solution of the maximum stable set problem.

    It is possible to exclude the fractional solution (0.5, 0.5, 0.5) by adding the condition that :math:`x` must be integer, but instead let us try to add an linear constraint that excludes it.  In order not to exclude the optimal solution, it is necessary to generate an expression which does not intersect the polyhedron of the stable set problem.  An inequality which does not exclude an optimal solution is called a *valid inequality*.  For example, :math:`x1 + x2 \leq 1` or :math:`x1 + x2 + x3 \leq 10` are valid inequalities.  Among the valid inequalities, those excluding the solution of the linear relaxation problem are called *cutting planes*.  For example, :math:`x_1 + x_2 + x_3 \leq 1` is a cutting plane.  In this example, the expression :math:`x_1 + x_2 + x_3 \leq 1` is in contact with the two-dimensional surface (a facet) of the polyhedron of the stable set problem.  Such an expression is called a *facet-defining* inequality.  Facets of the polyhedron of a problem are the strongest valid inequalities.

    

.. _tsp-mtz:

Miller-Tucker-Zemlin (potential) formulation
---------------------------------------------

.. index:: TSP: potential formulation
.. index:: TSP: Miller-Tucker-Zemlin formulation

           
.. _tsp-scf:

Single-commodity flow formulation
---------------------------------------------

.. index:: TSP: single-commodity flow formulation


.. _tsp-mcf:

Multi-commodity flow formulation
---------------------------------------------

.. index:: TSP: multi-commodity flow formulation




.. _tsptw:

Traveling Salesman Problem with Time Windows
============================================
           
.. index:: TSP with time windows


           
.. _cvrp:

Capacitated Vehicle Routing Problem
===================================

.. index:: capacitated vehicle routing problem



!!!!!!!!!!!!!!!!!!!



.. rubric:: Footnotes

.. [#f1-routing]  `networkX` is a Python module containing various algorithms for graphs, and can be downloaded from https://networkx.github.io
   
