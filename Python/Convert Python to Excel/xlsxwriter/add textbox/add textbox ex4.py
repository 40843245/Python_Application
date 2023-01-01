import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex4.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox with no border line',{'line': {'none': True}})

workbook.close()
