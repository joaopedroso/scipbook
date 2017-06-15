from pyscipopt import Model, quicksum, multidict

def flp(I,J,d,M,f,c):
    model = Model("flp")
    x,y = {},{}
    for j in J:
        y[j] = model.addVar(vtype="B", name="y(%s)"%j)
        for i in I:
            x[i,j] = model.addVar(vtype="C", name="x(%s,%s)"%(i,j))
    for i in I:
        model.addCons(quicksum(x[i,j] for j in J) == d[i], "Demand(%s)"%i)
    for j in M:
        model.addCons(quicksum(x[i,j] for i in I) <= M[j]*y[j], "Capacity(%s)"%i)
    for (i,j) in x:
        model.addCons(x[i,j] <= d[i]*y[j], "Strong(%s,%s)"%(i,j))
    model.setObjective(
        quicksum(f[j]*y[j] for j in J) +
        quicksum(c[i,j]*x[i,j] for i in I for j in J),
        "minimize")
    model.data = x,y
    return model
