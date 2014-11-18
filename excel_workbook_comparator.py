import pandas as pd
import os
import sys
import subprocess

def compare_worksheets(sheet1, sheet2):
    '''
        compare function if sheet1 and sheet2 are dataframes
    '''
    #subprocess.call(['diff', sheet1, sheet2])
    
def remove_sheet(sheet):
    subprocess.call(['rm', sheet])


if __name__ == '__main__':
f1 = sys.argv[2]
f2 = sys.argv[3]

xl_file1 = pd.ExcelFile(f1)
xl_file2 = pd.ExcelFile(f2)

N = len(xl_file1.sheet_names)
M = len(xl_file2.sheet_names)
assert (N==M), 'The two workbooks have different number of sheets'

for sheet_name1, sheet_name2 in zip(xl_file1.sheet_names, xl_file2.sheet_names):
    sheet1 = xl_file1.parse(sheet_name1)
    sheet2 = xl_file2.parse(sheet_name2)
    sheet1.to_csv('sheet1.csv', index=False)
    sheet2.to_csv('sheet2.csv', index=False)
    compare_worksheets('sheet1.csv', 'sheet2.csv')
    remove_sheet('sheet1.csv sheet2.csv')
