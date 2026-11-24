def simulatneous():
    Equations = [[]]*5
    unknowns = input("enter the number of unknowns: ")
    match unknowns:
        case 2:
            [x1,y1] = input("enter the coefficients of the terms: ")
            [x2,y2] = input("enter the coefficients of the terms: ")
            sEquation1 = [x1,y1]
            sEquation2 = [x2,y2] 
            Equations[0] = sEquation1
            Equation[1] = sEquation2   
            return simultaneousSolver(Equations, unkowns)     
        case 3:
            [x1,y1,z1] = input("Enter the coefficiants of the terms: ")
            [x2,y2,z2] = input("enter the coefficients of the terms: ")
            [x3,y3,z3] = input("enter the coefficients of the terms: ")
            sEquation1 = [x1,y1,z1]
            sEquation2 = [x2,y2,z2]
            sEquation3 = [x3,y3,z3]
            Equation[0] = sEquation1
            Equation[1] = sEquation2
            Equation[2] = sEquation3
            return simultaneousSolver(Equations, unknowns)
        case 4: 
            [x1,y1,z1,u1] = input("Enter the coefficiants of the terms: ")
            [x2,y2,z2,u2] = input("Enter the coefficiants of the terms: ")
            [x3,y3,z3,u3] = input("Enter the coefficiants of the terms: ")
            [x4,y4,z4,u4] = input("Enter the coefficiants of the terms: ")
            
            sEquation1 = [x1,y1,z1,u1]
            sEquation2 = [x2,y2,z2,u2]
            sEquation3 = [x3,y3,z3,u3]
            sEquation4 = [x4,y4,z4,u4]
            Equations[0] = sEquation1
            Equations[1] = sEquation2
            Equations[2] = sEquation3
            Equations[3] = sEquations4
            return simultaneousSolver(Equations, unknowns)
        case 5: 
            [x,y,z,u,v] = input("Enter the coefficiants of the terms: ")
            sEquation = [x,y,z,u,v] 
        case 6: 
            [x,y,z,u,v,w]
def simultaneousSolver2(Equations):
    multiplier = Equations[0][0]/Equations[1][0]
    Equations[1] = [multiplier * Equations[1][0], multiplier * Equations[1][1], mutiplier * Equations[1][2]
    Equations[0] = [0, Equations[0][1]-Equations[1][1], Equations[0][2]-Equations[1][2]]
    y= Equations[0][2]/Equations[0][1]
    x= (Equations[1][0]*x - Equations[1][2])/(-1* Equations[1][1])
    return x,y
def sinultaneousSolver3(Equations):
    multiplier =  Equations[0][2]/Equations[1][2]
    Equations[1] = [multiplier*Equations[1][0],multiplier*Equations[1][1], multiplier* Equations[1][2], multiplier* Equations[1][3]]
    Equations[1] = [Equations[0][0]-Equations[1][0],Equations[0][1]-Equations[1][1], Equations[0][3]-Equations[1][3]
    multiplier = Equations[0][2]/Equations[2][2]
    Equations[2] = [multiplier*Equations[2][0], multiplier*Equations[2][1], multiplier*Equations[2,2],multiplier * Equations[2][3]
    Equations[2] = [Equations[0][0]-Equations[2][0],Equations[0][1]-Equations[2,1],Equations[0,3]-Equations[2][3]
    
    
    temp = Equations[0]
   Equations[0] = Equations[1]
   Equations[1] = Equations[2]
   Equations[2] = temp
   [x,y] = simultaneousSolver2([Equations[0],Equations[1]])
   z=(Equations[2][0]*x+ Equations[2][1]*y - Equations[2][3])/(Equations[2][2]*(-1))
   
   return [x,y,z]
        