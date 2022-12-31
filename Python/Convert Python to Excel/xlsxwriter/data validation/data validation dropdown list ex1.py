import xlsxwriter
print('-------------------')    
workbook=xlsxwriter.Workbook("data_validation_ex4.xlsx")
worksheet=workbook.add_worksheet()
worksheet.data_validation('A4', {'validate': 'list',
                                 'source': ['open', 'high', 'close'],
                                 })
workbook.close()
print('-------------------')
