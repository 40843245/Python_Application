import xlsxwriter

workbook = xlsxwriter.Workbook('memory_management_ex2.xlsx',{'constant_memory': True})
worksheet = workbook.add_worksheet()

row_max=5
col_max=7
some_data="Hello"

# Not ok. With 'constant_memory' this will only write the first column of data.
for col in range(0, col_max):
    for row in range(0, row_max):
        worksheet.write(row, col, some_data)

workbook.close()
