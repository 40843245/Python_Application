import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex13.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'Text rotated up', {'text_rotation': 90})

workbook.close()
