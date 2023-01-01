import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex9.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox with color fill',{'fill': {'color': '#FF9900'}})

workbook.close()
