import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex12.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox with angle gradient',
                         {'gradient': {'colors': ['#DDEBCF', '#9CB86E', '#156B13'],
                                       'angle': 45}})

workbook.close()
