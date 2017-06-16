from pyscipopt import Model

model = Model("Simple linear optimization")

x = model.addVar(vtype="I", name="x")
y = model.addVar(vtype="I", name="y")
z = model.addVar(vtype="I", name="x")

model.addCons(x + y + z == 32,"Heads")
model.addCons(2*x + 4*y + 8*z == 80,"Legs")
model.setObjective(y + z, "minimize")

model.optimize()

if model.getStatus() == "optimal":
    print("Optimal value:", model.getObjVal())
    print("Solution:")
    print("  x = ", model.getVal(x))
    print("  y = ", model.getVal(y))
    print("  z = ", model.getVal(z))
else:
    print("Problem could not be solved to optimality")
