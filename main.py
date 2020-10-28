from dbservice import get_data_from_db
from excelservice import import_data_in_excel


def export_from_postgre_to_excel():
    rows = get_data_from_db()
    return import_data_in_excel(rows)


if __name__ == '__main__':
    export_from_postgre_to_excel()