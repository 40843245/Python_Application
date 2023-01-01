import xlsxwriter

workbook = xlsxwriter.Workbook('grouping_ex1.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_row(1, None, None, {'level': 1, 'hidden': True})
worksheet.set_row(2, None, None, {'level': 1, 'hidden': True})
worksheet.set_row(3, None, None, {'level': 1, 'hidden': True})
worksheet.set_row(4, None, None, {'level': 1, 'hidden': True})
worksheet.set_row(5, None, None, {'collapsed': True})

worksheet.set_column('B:G', None, None, {'level': 1, 'hidden': True})
worksheet.set_column('H:H', None, None, {'collapsed': True})

workbook.close()
