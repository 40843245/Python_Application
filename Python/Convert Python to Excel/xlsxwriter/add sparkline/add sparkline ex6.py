import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex6.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('A6', {'range': 'Sheet2!A1:J1',
                               'markers': True})

workbook.close()
