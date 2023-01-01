import xlsxwriter

workbook = xlsxwriter.Workbook('add_sparkline_ex16.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.add_sparkline('A18', {'range': 'Sheet2!A2:J2',
                                'type': 'column',
                                'series_color': '#E965E0'})

workbook.close()
