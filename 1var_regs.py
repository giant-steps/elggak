

### this is a group of single-variable regressions of passenger parameters vs. survival
    ### based on the titanic data set
### next step is to learn multivariate regression analysis, get r-squared value based on
    ### multiple parameters

## IMPORT STATEMENTS
import numpy as np
import csv
import sys
from scipy import stats

## FUNCTION DEFINITIONS



## MAIN FUNCTION
def main():
    ## read in .csv file from command line argument
        ### NOTE: all data must be able to be expressed as "float" objects
    reader = csv.reader(open(sys.argv[1]), delimiter=",")
    inp = list(reader)
    result = np.array(inp).astype("float")

    ## create dependent variable, "survival" (what we are trying to predict)
    dep_var = result[:,1]





## RUN MAIN FUNCTION
if __name__ == "__main__":
    main()

"""
    ***A note about the input file***
    Make sure there are no blanks. If placeholder is used for blanks, must deal with this.
    Make sure that the dependent variable is in the second column of the .csv file.
        (dep_var is set to result[:,1], so will look in second column)
    For each linear regression, ensure correct column is referenced for independent variable.

    
"""