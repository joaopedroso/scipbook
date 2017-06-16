"""
lo_simple.py: Simple SCIP example of linear programming:

maximize  15x + 18y + 30z
subject to 2x +   y +   z <= 60
           x  +  2y +   z <= 60
                        z <= 30
           x,y,z >= 0

Copyright (c) by Joao Pedro PEDROSO and Mikio KUBO, 2015
"""
from pyscipopt import Model

model = Model("Simple linear optimization")

x1 = model.addVar(vtype="C", name="x1")
x2 = model.addVar(vtype="C", name="x2")
x3 = model.addVar(vtype="C", name="x3")

model.addCons(2*x1 + x2 + x3 <= 60)
model.addCons(x1 + 2*x2 + x3 <= 60)
model.addCons(x3 <= 30)

model.setObjective(15*x1 + 18*x2 + 30*x3, "maximize")

model.optimize()

if model.getStatus() == "optimal":
    print("Optimal value:", model.getObjVal())
    print("Solution:")
    print("  x1 = ", model.getVal(x1))
    print("  x2 = ", model.getVal(x2))
    print("  x3 = ", model.getVal(x3))
else:
    print("Problem could not be solved to optimality")
