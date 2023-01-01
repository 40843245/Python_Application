import xlsxwriter

workbook = xlsxwriter.Workbook('write_comment_ex1.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.write('A1', 'Hello')
worksheet.write_comment('A1', 'This is a comment')

workbook.close()
