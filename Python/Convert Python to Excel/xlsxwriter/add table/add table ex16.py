import xlsxwriter

workbook = xlsxwriter.Workbook('add_table_ex16.xlsx')
worksheet = workbook.add_worksheet()

data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears',   2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges',  500,  300,  200,  700],
]
header_list=[
    {'total_string': 'Totals'},
    {'total_function': 'sum', 'total_value': 150},
    {'total_function': 'sum', 'total_value': 200},
    {'total_function': 'sum', 'total_value': 333},
    {'total_function': 'sum', 'total_value': 124},
    {'formula': '=SUM(Table10[@[Quarter 1]:[Quarter 4]])','total_function': 'sum','total_value': 807}
]
options = {'data': data,'total_row': 1,'columns':header_list }
workbook.close()
