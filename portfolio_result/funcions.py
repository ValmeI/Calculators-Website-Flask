from openpyxl import load_workbook

'# Excel headers'
headers = ["Kuupäev",
           "Kinnisvara puhas väärtus",
           "Füüsilise isiku aktsiad",
           "Juriidilise isiku aktsiad",
           "Aktsiad kokku",
           "Terve portfell kokku",
           "Mörr-i portfell",
           "Pere portfell kokku",
           "Vilde after Tax",
           "Vaba Raha",
           "Funderbeam Väärtus",
           "Kelly portfell kokku"]

'# path added just bc NAS cant understand where file is without it'


def get_excel_column(path, excel_name, column_letter):
    '# add file type'
    file_name = path + excel_name + ".xlsx"

    workbook_name = file_name
    wb = load_workbook(workbook_name)
    sheet1 = wb.active

    column_list = []
    '# using enumerate to get index and then to skip header row'
    for index, col in enumerate(sheet1[column_letter]):
        if index == 0:
            continue
        column_list.append(col.value)

    return column_list
