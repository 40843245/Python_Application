import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex8.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('A10', {'range': 'Sheet2!A1:J1',
                                'axis': True})

workbook.close()
