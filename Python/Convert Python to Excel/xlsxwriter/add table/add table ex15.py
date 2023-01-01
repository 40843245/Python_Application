import xlsxwriter

workbook = xlsxwriter.Workbook('add_table_ex15.xlsx')
worksheet = workbook.add_worksheet()

data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears',   2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges',  500,  300,  200,  700],
]

currency_format = workbook.add_format({'num_format': '$#,##0'})
wrap_format     = workbook.add_format({'text_wrap': 1})

header_list=[
    {'header': 'Product'},
    {'header': 'Quarter 1','total_function': 'sum','format': currency_format},
    {'header': 'Quarter 2','header_format': wrap_format,'total_function': 'sum','format': currency_format}
]
worksheet.add_table('B3:D8', {'data': data,'total_row': 1,'columns': header_list})
workbook.close()
