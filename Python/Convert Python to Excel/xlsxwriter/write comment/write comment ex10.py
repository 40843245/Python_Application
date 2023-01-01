import xlsxwriter

workbook = xlsxwriter.Workbook('write_comment_ex10.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.write('A1', 'Hello')
worksheet.write_comment('C3', 'Hello', {'start_col': 4})

workbook.close()
