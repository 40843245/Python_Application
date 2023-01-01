import xlsxwriter

workbook = xlsxwriter.Workbook('memory_management_ex1.xlsx',{'constant_memory': True})
worksheet = workbook.add_worksheet()

row_max=5
col_max=7
some_data="Hello"
# Ok. With 'constant_memory' you must write data in row by column order.
for row in range(0, row_max):
    for col in range(0, col_max):
        worksheet.write(row, col, some_data)

workbook.close()
