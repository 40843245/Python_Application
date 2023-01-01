import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex11.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('A7', {'range': 'Sheet2!A1:J1',
                               'high_point': True,
                               'low_point': True,
                               'first_point': True})

workbook.close()
