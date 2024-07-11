# -- START OF YOUR CODERUNNER SUBMISSION CODE
# INCLUDE ALL YOUR IMPORTS HERE

from dhCheck_Task2 import dhCheckCorrectness
def Task2(num, table, probs):

    # setting variables for later use
    prob1 = 0
    prob2 = 0
    # checks if x in teh table is greater than or equal to 1 or if it is less than or equal to 2 so it is between those collumns
    # checks if the x and y are added to be less than or eqal to 10 if it is either of the cases then it will be added to the variable 
    for y in range(len(table)):
        for x in range(len(table[0])):
            case1 = 1 <= x <= 2
            if  case1:
                prob1 += table[y][x] 
            if (x+2) + (y+6)  <= 10:
                prob2 += table[y][x]

    # gets the probability of prob1 and prob2 by dividing them by num
    prob1 = prob1/num
    prob2 = prob2/num


    # gets the probabilites of all the x collumns and times them by the probability 
    probx1 = (table[0][0] + table[1][0] + table[2][0]) * probs[0]
    probx2 = (table[0][1] + table[1][1] + table[2][1]) * probs[1]
    probx3 = (table[0][2] + table[1][2] + table[2][2]) * probs[2]
    probx4 = (table[0][3] + table[1][3] + table[2][3]) * probs[3]
    # adds all of the values for row 8 so it can be used to find out what the reverse probability is
    probOf8 = table[2][0] + table[2][1] + table[2][2] + table[2][3]
    # adds all of rows 6 and 7 and divides tehm by their probability 
    probOf6 = (table[0][0] + table[0][1] + table[0][2] + table[0][3])  *probs[4]
    probOf7 = (table[1][0] + table[1][1] + table[1][2] + table[1][3])  *probs[5]
    #gets the probabilty that there is a positive in the whole table
    probOfT = probx1+probx2+probx3+probx4
    #gets the reverse probability of row 8 and makes the probabilty of 8 and T variables probabilty for the next equations 
    prob8giveT = (probOfT -(probOf6 + probOf7))/ probOf8
    probOf8 = probOf8/120
    probOfT = probOfT/120
    # uses bayes theorem to get the probabilty that on row 8 there is a positive hit
    prob3 = (prob8giveT*probOf8)/ probOfT 

    return (prob1, prob2, prob3)

# -- END OF YOUR CODERUNNER SUBMISSION CODE
