import xlsxwriter
print('-------------------')    
workbook=xlsxwriter.Workbook("data_validation_ex3.xlsx")
worksheet=workbook.add_worksheet()
worksheet.data_validation('B2', {'validate': 'integer',
                                  'criteria': 'between',
                                  'minimum': 1,
                                  'maximum': -100,
                                  'input_title': 'Enter an integer:',
                                  'input_message': 'between 1 and -100'})
workbook.close()
print('-------------------')

"""
NOTE that:
In this example,
the jupyter notebook does neither throw error when compiling, throw exception when running.
And the Microsoft Excel doesn't throw any exception when opening file.
It just works as usual which is same as the previous example.
Thus, whenever the value of B2 you enter, the constraint of value of B2 is always NOT satisfied. 
Hence, throwing exception when enter value of B2.
"""
