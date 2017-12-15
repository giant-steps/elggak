
# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import statsmodels.api as sm
import pandas as pd

# MAIN FUNCTION
def main():

    reader = csv.reader(open(sys.argv[1]), delimiter="\t")
    inp = list(reader)
    points = np.array(inp).astype("str")      ## must change to string for now
    ### data1.csv, for now: 0:9 : PassID,Surv,pclass,sex,age,sibsp,parch,fare,cabin,embarked
        #remember: row,column

    print(points)     ############

    ## vino1.csv fields:    points, title, variety, description, country, province, region1, region2,
    ##                          winery, designation, price, taster name, taster twitter handle

    ## order in file: number, country, description, designation, points, price, prov, reg1, reg2,
            ## variety, winery

    aa = points[:,3]
    bb = points[:,1]      ### for single variable OLS, use this to choose independent variable

    cc = points[:,2:10]

    X = cc      #### X = aa, or X = cc for multiple variables
    y = bb

    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)

    #print(model.summary())

    """
    ypred = model.predict(X)

    """



# RUN MAIN FUNCTION
if __name__ == "__main__":
    main()
