# access aws 
def basicS3Access():
    """
    Basic example of how to access AWS s3 buckets.
    
    Input: none
    Output: none
    """
    import boto3
    s3 = boto3.resource('s3')
    for b in s3.buckets.all():
        print(b.name)

# credentials for connecting to the MySQL db
db_creds = {'user': 'captecher',
            'password': '123data',
            'host': 'captechbootcamp.cat1vmhhjrmh.us-east-1.rds.amazonaws.com',
            'database':'Bootcamp'}

def getDBCursor(creds):
    """
    Get the cursor for the db to perform transaction.

    Input: creds (dictionary of login credentials)
    Output: MySQL Connection, MySQl cursor object
    """
    cnx = mysql.connector.connect(**creds)
    return cnx, cnx.cursor()

def queryDB(cursor, query):
    """
    Execute a sql query.

    Input: cursor (MySQL cursor object), query (string of sql query)
    Output: dictionary containing the lines of the query
    """
    cursor.execute(query)
    return cursor.fetchall()


def executeQuery(creds, query):
    """
    Executes a query by connecting, querying, and closes the db connection

    Input: creds (db login credentials), query (string of sql query)
    Output: dictionary of query results
    """
    import mysql.connector
    result = None
    try:
        conn, cursor = getDBCursor(creds)
        result = queryDB(cursor, query)
    except Error as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
    return result