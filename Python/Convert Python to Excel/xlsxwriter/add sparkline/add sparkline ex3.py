import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex3.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('F1', {'range': "'Monthly Data'!A1:E1"})

workbook.close()
