# -- START OF YOUR CODERUNNER SUBMISSION CODE
# INCLUDE ALL YOUR IMPORTS HERE
import numpy as np
from scipy.optimize import linprog
from dhCheck_Task3 import dhCheckCorrectness
def Task3(x, y, z, x_initial, c, x_bound, se_bound, ml_bound):
    
    # Transpose x array to match the shape for the linear regression
    x_transposed = np.array(x).T
    
    # Prepare X for linear regression
    X = np.column_stack((np.ones(len(x_transposed)), x_transposed))

    # linear regression for y
    weights_b = np.linalg.lstsq(X, y, rcond=None)[0]

    # linear regression for z
    weights_d = np.linalg.lstsq(X, z, rcond=None)[0]

    #creating y and z values so they can be used in b_ie calculation  
    Y = weights_b[0] + weights_b[1]* x_initial[0]+ weights_b[2]* x_initial[1]+ weights_b[3]* x_initial[2]+ weights_b[4]* x_initial[3]
    Z = weights_d[0] + weights_d[1]* x_initial[0]+ weights_d[2]* x_initial[1]+ weights_d[3]* x_initial[2]+ weights_d[4]* x_initial[3]

    # Define the bounds for each additional security control
    bounds = [(0, bound) for bound in x_bound]

    # Define the inequality constraints matrix (A_ie) and the inequality constraints vector (b_ie)
    A_ie = np.vstack([-weights_b[1:], weights_d[1:]])
    b_ie = np.array([-se_bound + Y, ml_bound -Z])
    A_eq =None
    b_eq =None

    # Define the coefficients for the objective function
    c = np.array(c)

    # Solve the linear programming problem
    result = linprog(c=c, A_ub=A_ie, b_ub=b_ie, A_eq = A_eq ,b_eq= b_eq, bounds=bounds)

    # Extract the additional security controls from the solution
    x_add = result.x

    return weights_b, weights_d, x_add
# -- END OF YOUR CODERUNNER SUBMISSION CODE
