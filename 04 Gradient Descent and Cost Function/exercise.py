import numpy as np
import pandas as pd
import math
def gradient_descent(x,y):
    m_curr = b_curr =0
    iterations = 1000000
    n=len(x)
    learning_rate = 0.0001


    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        if(i==0):
            cost_n1 = 0
        else:
            cost_n1 =cost
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        print(cost_n1)
        if(math.isclose(cost_n1,cost,rel_tol=1e-20)):
            break
        md = -(2/n)* sum(x*(y-y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr -learning_rate *md
        b_curr = b_curr - learning_rate * bd
        print("m {} b {}, cost {} cost_n {} iteration {}".format(m_curr,b_curr, cost,cost_n1,i))

df = pd.read_csv('test_scores.csv')
x = df['math']
y= df['cs']
#print(df,end="\n")
#print(x,y,end="\n",sep="\n")
#x= np.array([1,2,3,4,5])
#y=np.array([5,7,9,11,13])
gradient_descent(x,y)