from sympy.solvers import solve
from sympy import Symbol
from sympy import cos, pi, sin
import sympy
import math

minOmega = 1
maxOmega = 100
omegaStep = 1
omegaDivider = 10

alpha = 1.0/1.797

results = list() #(omega, amplitude)

for bigOmega in range(minOmega, maxOmega, omegaStep):
    omega = bigOmega / omegaDivider
    print("omega = " + str(omega))
    def q(t): 
        1/(omega**2 + alpha**2) * (alpha * math.sin(omega * t) - omega * math.cos(omega * t))
    
    tSym = Symbol('tSym')    #symbolic t
    qDerSolutions = solve([alpha*sympy.cos(omega*tSym) + omega*sympy.sin(omega*tSym), tSym >= 0, tSym <= 2*pi/omega], tSym)
    print("q extreme points are at: " + str(qDerSolutions))
    
    extremeQValues = list()
    for solution in qDerSolutions:
        extremeQValues.append(q(solution))
    print(extremeQValues)
    
    minQValue = min(extremeQValues)
    maxQValue = max(extremeQValues)
    amplitude = maxQValue - minQValue
    results.append((omega, amplitude))
    
 #todo: take results and draw plot
