import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex16.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('A1', 'This is some text',
                         {'url': 'https://github.com/jmcnamara'})

workbook.close()
