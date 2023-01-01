import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex6.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox with larger border',{'line': {'width': 3.25}})


workbook.close()
