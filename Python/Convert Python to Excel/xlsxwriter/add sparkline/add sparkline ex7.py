import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex7.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('A9', {'range': 'Sheet2!A1:J1',
                               'negative_points': True})

workbook.close()
