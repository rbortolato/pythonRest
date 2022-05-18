import jaydebeapi

def initialize():
    execute('DROP TABLE IF EXISTS premiacao;')
    execute('CREATE TABLE IF NOT EXISTS premiacao (produtor VARCHAR NOT NULL, ano SIGNED NOT NULL)')

def execute(query, ret=None):    
    connection  = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbc:h2:tcp://localhost:5234/myApp/database/db",
        ["SA", ""],
        ".\myApp\database\h2-2.1.212.jar")

    cursor = connection.cursor()
    cursor.execute(query)

    if ret:
        ret = convert(cursor)
    
    cursor.close()
    connection.close()

    return ret

def convert(cursor):
    column_names = [record[0].lower() for record in cursor.description]
    return [dict(zip(column_names, record)) for record in cursor.fetchall()]