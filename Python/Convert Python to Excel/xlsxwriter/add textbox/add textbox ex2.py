import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex2.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'Size adjusted textbox',{'x_offset':10,'y_offset':30,
                                                        'width': 288, 'height': 30})

# or ...
worksheet.insert_textbox('B2', 'Size adjusted textbox',{'x_offset':10,'y_offset':120,
                                                        'x_scale': 1.5, 'y_scale': 0.25})

workbook.close()
