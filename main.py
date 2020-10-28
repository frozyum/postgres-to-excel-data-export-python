from dbservice import get_data_from_db, import_data_in_db
from excelservice import import_data_in_excel, export_data_from_excel


def export_from_postgre_to_excel():
    rows = get_data_from_db()
    return import_data_in_excel(rows)


def export_from_excel_to_postgre():
    rows = export_data_from_excel()
    return import_data_in_db(rows)


if __name__ == '__main__':
    export_from_postgre_to_excel()
