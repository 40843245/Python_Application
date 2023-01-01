import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex3.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', "Don't move or size with cells",{'object_position': 3})

workbook.close()
