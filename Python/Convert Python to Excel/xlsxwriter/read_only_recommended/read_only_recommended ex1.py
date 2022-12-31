import xlsxwriter

workbook = xlsxwriter.Workbook('file.xlsx')
worksheet = workbook.add_worksheet()

workbook.read_only_recommended()

workbook.close()
