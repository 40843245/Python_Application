import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex10.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

worksheet.insert_textbox('B2', 'A textbox with gradient fill',
                         {'gradient': {'colors':['#DDEBCF', '#156B13'],'positions': [10,90]}})

workbook.close()
