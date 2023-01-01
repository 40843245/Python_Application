import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex11.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox with gradient fill',
                         {'gradient': {'colors': ['#DDEBCF', '#9CB86E', '#156B13'],
                                       'type': 'radial'}})

workbook.close()
