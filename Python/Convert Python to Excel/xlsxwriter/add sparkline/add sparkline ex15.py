import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex15.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('F3', {'range': 'A3:E3',
                               'date_axis': 'A4:E4'})

workbook.close()
