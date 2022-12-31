import xlsxwriter
print('-------------------')    
workbook=xlsxwriter.Workbook("data_validation_ex1.xlsx")
worksheet=workbook.add_worksheet()
worksheet.data_validation('B2', {'validate': 'integer',
                                  'criteria': 'between',
                                  'minimum': 1,
                                  'maximum': 100,
                                  'input_title': 'Enter an integer:',
                                  'input_message': 'between 1 and 100'})
workbook.close()
print('-------------------')
