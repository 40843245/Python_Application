import xlsxwriter

workbook = xlsxwriter.Workbook('write_comment_ex11.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.write('A1', 'Hello')
worksheet.write_comment('C3', 'This is a comment', {'x_offset': 30})

workbook.close()
