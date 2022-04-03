import pyodbc


class SQL_Server:
    def __init__(self):
        server = 'DESKTOP-8TG1B6T\SQLEXPRESS'
        database = 'bikerStore'
        username = 'sa'
        password = 'long2001'
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                   server+';DATABASE='+database+';Trusted_Connection=yes;UID='+username+';PWD=' + password)

    def search_item(self, item):
        query = "SELECT p.product_name, b.brand_name, c.category_name, p.list_price FROM products as p,brands as b,categories as c WHERE product_name like '%{}%' AND p.brand_id = b.brand_id AND p.category_id = c.category_id".format(
            item)
        print(query)
        cursor = self.cnxn.cursor()
        cursor.execute(query)

        data = []
        for row in cursor:
            data.append(row)
        self.cnxn.commit()
        return data, query

    def select_by_name_pass(self, name, password):
        query = "SELECT * FROM Users WHERE name = '{}' and password = '{}'".format(
            name, password)
        print(query)
        cursor = self.cnxn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()

        if data:
            return True, query
        else:
            return False, query


if __name__ == "__main__":
    sql = SQL_Server()
    # name = input()
    # password = input()

    # query = "SELECT * FROM Users WHERE name = '{}' and password = '{}'".format(
    #     name, password)

    # # Execute query
    # print(query)
    # data = sql.select(query)
    # print(data == None)

    data = sql.search_item('2016')
    print(data)
