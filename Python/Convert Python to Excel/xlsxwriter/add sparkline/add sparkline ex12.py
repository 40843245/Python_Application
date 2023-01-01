import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex12.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('F1', {'range': 'A1:E1',
                               'max': 0.5,
                               'min': -0.5})

workbook.close()
