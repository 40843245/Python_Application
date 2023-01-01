import xlsxwriter

workbook = xlsxwriter.Workbook('add_textbox_ex1.xlsx')
worksheet = workbook.add_worksheet()

text = 'Formatted textbox'

options = {
    'width': 256,
    'height': 100,
    'x_offset': 10,
    'y_offset': 10,

    'font': {'color': 'red','size': 14},
    'align': {'vertical': 'middle','horizontal': 'center'},
    'gradient': {'colors': ['#DDEBCF','#9CB86E','#156B13']},
}

worksheet.insert_textbox('B2', text, options)

workbook.close()
