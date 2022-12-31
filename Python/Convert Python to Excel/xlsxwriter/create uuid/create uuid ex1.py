import xlsxwriter
import uuid

def write_uuid(worksheet, row, col, uuid, format=None):
    return worksheet.write_string(row, col, str(uuid), format)

def test():
    workbook=xlsxwriter.Workbook("UUID_ex1.xlsx")
    worksheet=workbook.add_worksheet()
    
    #                           match,     action()
    worksheet.add_write_handler(uuid.UUID, write_uuid)

    my_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')

    # Write the UUID. This would raise a TypeError without the handler.
    worksheet.write('A1', my_uuid)
    
    workbook.close()
#driver code
test()
