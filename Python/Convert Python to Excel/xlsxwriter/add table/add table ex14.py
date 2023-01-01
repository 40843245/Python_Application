import xlsxwriter

workbook = xlsxwriter.Workbook('add_table_ex14.xlsx')
worksheet = workbook.add_worksheet()

data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears',   2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges',  500,  300,  200,  700],
]
formula = '=SUM(Table8[@[Quarter 1]:[Quarter 4]])'
header='header'
header_list = [
    {header: 'Product'},
    {header: 'Quarter 1'},
    {header: 'Quarter 2'},
    {header: 'Quarter 3'},
    {header: 'Quarter 4'},
    {header: 'Year','formula': formula},
]
worksheet.add_table('B3:F7', {'data': data,
                              'columns':header_list})
workbook.close()
