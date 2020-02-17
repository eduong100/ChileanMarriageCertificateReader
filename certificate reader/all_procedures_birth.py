#!/usr/bin/env python

from overfiles import create_file_list
from iter import extractTextList, pdf_to_list
from birth import combined
from excel_2 import append_df_to_excel
import numpy as np
import pandas as pd

def everything(directory, first, last):
    a = create_file_list(directory)
    if '.pdf' not in a[first]:
        while '.pdf' not in a[first]:
            first = first + 1
    if last in range(len(a)):
        b = a[first:last]
    else:
        b = a[first:]
    x = 0
    for file in b:
        text_elements = pdf_to_list(directory + '/' + file)
        try:
            list = combined(text_elements)
        except IndexError:
            list = [file, 'Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error']
        data = np.array([['Column 0', 'Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7'], list])
        df = pd.DataFrame(data=data[1:,0:])
        append_df_to_excel('output_nac.xlsx', df)
