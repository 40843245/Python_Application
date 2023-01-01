import xlsxwriter

workbook = xlsxwriter.Workbook('write_comment_ex2.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.write('A1', 'Hello')
worksheet.write_comment('C3', 'Hello', {'x_scale': 1.2, 'y_scale': 0.8})

workbook.close()
