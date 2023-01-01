import xlsxwriter

workbook = xlsxwriter.Workbook('write_comment_ex4.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.write('A1', 'Hello')
worksheet.set_comments_author('John Smith')

workbook.close()
