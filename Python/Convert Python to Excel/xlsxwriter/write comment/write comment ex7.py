import xlsxwriter

workbook = xlsxwriter.Workbook('write_comment_ex7.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.write('A1', 'Hello')
worksheet.write_comment('C3', 'Hello', {'x_scale': 2  })
worksheet.write_comment('C4', 'Hello', {'x_scale': 4.2})

workbook.close()
