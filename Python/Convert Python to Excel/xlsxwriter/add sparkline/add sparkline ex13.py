import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex13.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('F1', {'range': 'A1:E1',
                               'empty_cells': 'zero'})

workbook.close()
