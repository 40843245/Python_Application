import xlsxwriter

workbook = xlsxwriter.Workbook('add_table_ex4.xlsx')
worksheet = workbook.add_worksheet()

data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears',   2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges',  500,  300,  200,  700],
]
# Turn off banded rows.
worksheet.add_table('B3:F7', {'banded_rows': False})
workbook.close()