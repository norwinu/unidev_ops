import ibm_db_dbi as dbi

print('Test DB2 Connect.')

def listRecords():
    try:
        db2conn = dbi.connect(dsn=None, database='*LOCAL', user=None, password=None)
        db2curry = db2conn.cursor()
        db2curry.execute("SELECT * FROM WEBPRDD.POSFTPUSRP")
        result = db2curry.fetchall()
        print(result)
        print(type(result))
    except Exception as e:
        return 'Exception' + str(e)

listRecords()