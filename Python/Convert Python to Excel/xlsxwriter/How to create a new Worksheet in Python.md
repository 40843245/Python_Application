# How to create a new Worksheet in Python?
Call the method add_worksheet method for the object with type Workbook.

For example,

workbook = xlsxwriter.Workbook('sample.xlsx')
worksheet = workbook.add_worksheet()

will create a enw empty Workbook named sample.xlsx 
and add a new empty worksheet in sample.xlsx.

