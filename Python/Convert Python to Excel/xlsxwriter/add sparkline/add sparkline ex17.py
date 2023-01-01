import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex17.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('A27', {'location': ['A27',   'A28',   'A29'],
                                'range':    ['A5:J5', 'A6:J6', 'A7:J7']})

workbook.close()
