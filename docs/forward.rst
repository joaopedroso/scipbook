.. _forward:

********************************************************************************
Forward
********************************************************************************


.. rubric:: Forward

This book is loosely based on *“Mathematical Optimization: Solving Problems using Python and Gurobi”* by M. Kubo, J.P. Pedroso, M. Muramatsu, and A. Rais, in Japanese, published in 2012 by Kindaikagakusha in Tokyo. Readers fluent in Japanese and aiming at using Gurobi as a solver are kindly directed to that book.  Our interests in preparing this version in English are twofold: we wish to widen the readership, and we would like to give the possibility of using a cutting edge solver to potential users who prefer the licensing policy of SCIP.

This book is an open project: we expect that new editions will incorporate contributions by our readers and SCIP users, and to extend it to exploit SCIP's potential in some specific areas, in particular nonlinear optimization.

Formulations and programs proposed in the book have been extensively tested computationally; the results are available in XXXXXX. % !!!!



.. rubric:: Forward to the Japanese edition

Mathematical optimization (previously known as *mathematical programming*), is a branch of applied mathematics with more than half a century history.  Being an area where the theory and abundant and elegant applications, it has been called the queen of applied mathematics.

In this book, rather than presenting an old-fashioned, theoretical introduction the mathematical optimization, our intention is to provide the basis for mastering the technique of solving the problem at hand by means of an "optimization solver", unveiling tricks and tips to model and solve real-world problems.

Solving mathematical optimization problems involves extensive numerical calculations.  It required acquaintance with computers and proficiency in specialized programming languages, besides familiarity with mathematical modeling and optimization algorithms.  The hurdle was very high, and it was extremely rare for companies to have human resources making full use of the power of mathematical optimization for solving their real problems.

Recently, however, mathematical optimization problems became easily solvable by means of general-purpose, high performance solvers.  Besides, currently available very high-level programming languages significantly reduced the barrier for actually using these solvers.  Therefore, it became possible to quickly tackle even very complex real-world problems.

In order to respond to such changes in paradigm, it was the authors intention to write a new type of introduction to mathematical optimization.  As much as possible, the theoretical descriptions have been limited to subjects that are useful in practice.  There is no hindrance to the usage of a mathematical optimization solver as black box, because there is no need to know all of its details for successfully using it.  Nevertheless, as most of the practical problems involving combinatorial optimization belong to the class of to the so-called NP-hard problems, it can not be avoided that their solution can be very time consuming.  Therefore, for successfully tackling these problems it is necessary a basic understanding of the theory, along with some modeling tricks.  In this book, as well as commented examples of using the basic theory, we provide the readers with indications on how correctly and quickly solve practical problems.  We hope this book will be a primer for the usage of mathematical optimization in a new era.

The information contained in this document is as follows.
Chapter 1 is an introduction to the basics of mathematical optimization.
First of all, it presents the terminology and the most fundamental class of mathematical optimization problems, the linear optimization problem.  Then, it explains with examples how to formulate simple models and how to use a mathematical optimization solver to find a solution.

In the section presenting the transportation problem it will be explained the concept of duality.  Besides its practical applications, duality allows a better understanding the theory underlying linear optimization.
In the section of the multi-constraint knapsack problem we explain the basic solving technique for problems involving integer variables, the branch and bound method.
In the section concerning the nutrition problem we discuss the case where there is no optimal solution (infeasible or unbounded instances), and propose workarounds.

..  complete this description -- simple linear optimization problem to an example, crane and tortoise puzzle, transportation problem, multi-product transportation problem, mixed problem, fractional optimization problem, multi-constraint knapsack problem, is a nutritional problem.
   
In Chapter 2, we describe some precautions that should be taken when formulating integer optimization problems.  Illustrations include the capacity constrained facility location problem, the $k-$\ median problem, and a commented example of the $k-$\ center problem.

In the third chapter we introduce a formulation for the bin packing problem.  We present a formulation for the variant called the cutting stock problem, and introduce a solution technique that utilizes duality, in the so-called column generation approach.

In the fourth chapter, we introduce combinatorial optimization problems related to graphs: the graph partitioning problem, the maximum stable set problem, and the graph coloring problem.  In the section on the graph coloring problem, we describe an ingenuous formulation to deal with symmetry.

Chapter 5 describes routing problems.  After dealing with the basic traveling salesman problem, we propose a formulation for this problem with time windows, and some formulations for the capacity constrained vehicle routing problem.  In addition, sections of the traveling salesman problem introduce the cutting plane method.

.. and the lifting operation ???

Chapter 6 focuses on scheduling problems. Several types of formulation are proposed; the one to select depends on particular case at issue.

In Chapter 7 the dynamic lot sizing problem is analyzed with formulations for the multiple item case, and for the multi-stage lot sizing problem.

Chapter 8 describes techniques to approximate a nonlinear function with a piecewise linear function, explaining the concept of special ordered set.

.. etc etc

Chapter 9 deals with multi-objective optimization, describing the basic theory and the usage of SCIP/Python for solving this class of problems

.. etc etc

   
