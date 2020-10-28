import xlsxwriter


def import_data_in_excel(rows):
    workbook = xlsxwriter.Workbook('salaries.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for e in rows:
        for j in e:
            worksheet.write(row, col, j)
            col += 1
        row += 1
        col = 0
    workbook.close()
    return 'salaries.xlsx'
