import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex9.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('A24', {'range': 'Sheet2!A4:J4',
                                'type': 'column',
                                'style': 20,
                                'reverse': True})

workbook.close()
