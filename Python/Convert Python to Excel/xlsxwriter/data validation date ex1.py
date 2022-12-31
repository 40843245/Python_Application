import xlsxwriter
print('-------------------')    
workbook=xlsxwriter.Workbook("data_validation_ex6.xlsx")
worksheet=workbook.add_worksheet()
from datetime import date

worksheet.data_validation('A6', {'validate': 'date',
                                 'criteria': 'between',
                                 'minimum': date(2013, 1, 1),
                                 'maximum': date(2013, 12, 12),
                                 })
workbook.close()
print('-------------------')
