import xlsxwriter

workbook = xlsxwriter.Workbook('add_table_ex7.xlsx')
worksheet = workbook.add_worksheet()

data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears',   2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges',  500,  300,  200,  700],
]
# Turn on highlighting for the last column in the table.
worksheet.add_table('B3:F7', {'last_column': True})
workbook.close()
