import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex2.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('F1', {'range': 'Sheet2!A1:E1'})

workbook.close()
