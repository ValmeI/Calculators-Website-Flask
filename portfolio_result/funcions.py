import xlrd

'# headrid mida exceli loogmisel ja updateimisel kasutatakse'
headers = {0: "Kuupäev",
           1: "Kinnisvara puhas väärtus",
           2: "Füüsilise isiku aktsiad",
           3: "Juriidilise isiku aktsiad",
           4: "Aktsiad kokku",
           5: "Terve portfell kokku",
           6: "Mörr-i portfell",
           7: "Pere portfell kokku",
           8: "Vilde after Tax",
           9: "Vaba Raha",
           10: "Funderbeam Väärtus",
           11: "Kelly portfell kokku"}


def get_excel_column(path, excel_name, column_number):
    column_list = []
    '# Kergem anda sisendisse 1 tulp ning hiljem -1 teha kuna lugemine hakkab 0ist'
    column_number = column_number-1
    '# lisab file type'
    file_name = excel_name + ".xls"
    '# open excel file'
    rb = xlrd.open_workbook(path + file_name)
    first_sheet = rb.sheet_by_index(0)

    for col in first_sheet.col_values(column_number):
        '# kõik string siis ei tule errorit, vajadus et header ei tuleks listi'
        if str(col) in headers.get(column_number):
            continue
        column_list.append(col)
    return column_list