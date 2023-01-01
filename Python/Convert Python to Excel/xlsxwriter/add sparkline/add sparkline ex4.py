import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex4.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('F2', {'range': 'A2:E2',
                               'type': 'column'})

workbook.close()
