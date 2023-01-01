import xlsxwriter

workbook = xlsxwriter.Workbook('write_comment_ex6.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.write('A1', 'Hello')
worksheet.write_comment('C3', 'Hello', {'visible': False})

workbook.close()
