
#this program should read in data in an excel file (or .csv file?) and be able to manipulate it

# ensure that the necessary mods are installed by entering the following into the command line:
    #pip install xlrd
    #pip install xlwt

#first command line argument is file to be parsed, second is number of columns

import xlrd
import sys




def main():
    imp = sys.argv[1]

    num_col = sys.argv[2]

    workbook  = xlrd.open_workbook(imp)

    worksheet = workbook.sheet_by_index(0)

    while True:     ##### CHANGE THIS

        a = 0
        while a < num_col:
            worksheet.cell
            a += 1

if __name__ == "__main__":
    main()

