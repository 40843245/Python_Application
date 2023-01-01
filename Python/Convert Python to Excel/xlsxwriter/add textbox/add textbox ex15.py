import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex15.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('A2', None, {'textlink': '=Sheet2!A1'})

workbook.close()
