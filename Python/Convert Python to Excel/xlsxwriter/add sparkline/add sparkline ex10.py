import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex10.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('F2', {'range': 'A2:E2',
                               'weight': 0.25})

workbook.close()
