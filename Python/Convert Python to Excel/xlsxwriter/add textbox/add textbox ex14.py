import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex14.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('A1', '', {'textlink': '=$A$1'})

workbook.close()
