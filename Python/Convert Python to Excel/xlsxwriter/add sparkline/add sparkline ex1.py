import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex1.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline(0, 5, {'range': 'Sheet1!A1:E1'})

workbook.close()
