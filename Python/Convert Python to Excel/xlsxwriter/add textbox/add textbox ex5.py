import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex5.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox with a color border',{'line': {'color': 'red'}})

workbook.close()
