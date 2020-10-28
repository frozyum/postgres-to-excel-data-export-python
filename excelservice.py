import xlsxwriter
import xlrd


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


def export_data_from_excel():
    loc = "salaries.xlsx"

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    rows = []
    for i in range(sheet.nrows):
        rows.append(sheet.row_values(i))
    return rows

