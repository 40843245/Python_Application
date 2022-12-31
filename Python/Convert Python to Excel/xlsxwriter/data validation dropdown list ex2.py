import xlsxwriter
print('-------------------')    
workbook=xlsxwriter.Workbook("data_validation_ex5.xlsx")
worksheet=workbook.add_worksheet()
worksheet.data_validation('A5', {'validate': 'list',
                                 'source': '=$A$1:$I$1',
                                 })
workbook.close()
print('-------------------')
