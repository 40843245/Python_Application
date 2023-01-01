import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex14.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('F3', {'range': 'A3:E3',
                               'show_hidden': True})

workbook.close()
