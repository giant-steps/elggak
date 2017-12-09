

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
    reader = csv.reader(open(sys.argv[1]), delimiter="\t")
    inp = list(reader)

    ###PassengerId;Survived;Pclass;Name;Sex;Age;SibSp;Parch;Ticket;Fare;Cabin;Embarked
    ### name removed, embarked: 1=S, 2=C, 3=Q, ticket removed for now
    ### can do more w/ Cabin field, first will be rudimentary -- blanks w/ placeholder, letter to num code
        ### For cabin, 1=A, 7=G, etc. -- room numbers not taken into account -- missing is 3.5

    ### data1.csv, for now: 0:9 : PassID,Surv,pclass,sex,age,sibsp,parch,fare,cabin,embarked

    inp2 = inp[1:]
    result = np.array(inp2).astype("float")
    #print(str(result))

    ## create dependent variable, "survival" (what we are trying to predict)
    dep_var = result[:,1]

    #########################
    ## create independent variables, there are 8 of them for now -- running simple linear
        ## regressions for each -- then move into multivariate regression analysis


    ###regression -- pclass & survival
    ind_var_pclass = result[:,2]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_pclass, dep_var)
    pclass_correlation = r_value**2
    print("Survival based on social class: " + (str(pclass_correlation)))

    ###regression -- sex & survival
    ind_var_sex = result[:,3]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_sex, dep_var)
    sex_correlation = r_value**2
    print("Survival based on sex: " + (str(sex_correlation)))

    ###regression -- age & survival
    ind_var_age = result[:,4]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_age, dep_var)
    age_correlation = r_value**2
    #print("Survival based on age: " + (str(age_correlation)))

    ###regression -- sibsp & survival
    ind_var_sibsp = result[:,5]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_sibsp, dep_var)
    sibsp_correlation = r_value**2
    #print("Survival based on sibsp: " + (str(sibsp_correlation)))

    ###regression -- parch & survival
    ind_var_parch = result[:,6]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_parch, dep_var)
    parch_correlation = r_value**2
    #print("Survival based on parch: " + (str(parch_correlation)))

    ###regression -- fare & survival
    ind_var_fare = result[:,7]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_fare, dep_var)
    fare_correlation = r_value**2
    print("Survival based on fare: " + (str(fare_correlation)))

    ###regression -- cabin & survival
    ind_var_cabin = result[:,8]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_cabin, dep_var)
    cabin_correlation = r_value**2
    #print("Survival based on cabin: " + (str(cabin_correlation)))

    ###regression -- emb & survival
    ind_var_emb = result[:,9]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_emb, dep_var)
    emb_correlation = r_value**2
    #print("Survival based on emb: " + (str(emb_correlation)))

    ###########################
    """

    342/891 survived (in training set)
    so assume base survival rate of 0.38384
    this will be raised or lowered based on 3 parameters






    Base score is 0.38384

    If final score is less than 0.5, survived is 0, if greater, survived is 1
    What percent of survival predictions are correct? This is efficacy of model
    Weight each variable based on rsquared from linear regression
    Obviously this is cruder than multivariate analysis, but start here
    If age rsquared is 0.3, age over max times 0.3
    That value multiplied by base score
    Once base score has been altered by all 8, plug in to get final score

    NEXT
    break age into ranges, etc.
    """
    ###########################



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