

### learn pandas

# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
from scipy import stats
from pylab import plot,show
import statsmodels.api as sm
import pandas as pd
from sklearn import datasets


# MAIN FUNCTION
def main():

    reader = csv.reader(open(sys.argv[1]), delimiter="\t")
    inp = list(reader)
    points = np.array(inp).astype("float")
    ### data1.csv, for now: 0:9 : PassID,Surv,pclass,sex,age,sibsp,parch,fare,cabin,embarked
        #remember: row,column

    #print(str(points))     ############

    aa = points[:,3]
    bb = points[:,1]      ### for single variable OLS, use this to choose independent variable

    data = datasets.load_boston()

    #print(data.DESCR)

    df = pd.DataFrame(data.data, columns=data.feature_names)
    target = pd.DataFrame(data.target, columns=["MEDV"])

    ##X = df["RM"]
    ##y = target["MEDV"]
    X = aa
    y = bb

    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)

    print(model.summary())




# RUN MAIN FUNCTION
if __name__ == "__main__": 
    main()

