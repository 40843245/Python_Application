import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex8.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox with no fill',{'fill': {'none': True}})

workbook.close()
