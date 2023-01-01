import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex7.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox a dash border',{'line': {'dash_type': 'dash_dot'}})

workbook.close()
