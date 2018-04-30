from sems import app,mysql

class DAOClass():

    def __init__(self):
        self.db=None

    def connect(self):        
        self.db=mysql.connect(app.config.get('MYSQL_DATABASE_HOST'),
	    app.config.get('MYSQL_DATABASE_USER'),
	    app.config.get('MYSQL_DATABASE_PASSWORD'),
	    app.config.get('MYSQL_DATABASE_DB'))

        """
        self.db=mysql.connect(app.config['MYSQL_DATABASE_HOST'],
	    app.config['MYSQL_DATABASE_USER'],
	    app.config['MYSQL_DATABASE_PASSWORD'],
	    app.config['MYSQL_DATABASE_DB'])
        """

    def disconnect(self):
        self.db.close()


    def updateData(self,sql):
        self.connect()
        cursor=self.db.cursor()
        r=False
        try:
            rowsaffected=cursor.execute(sql)
            if(rowsaffected>0):
                r=True
                self.db.commit()
        except:
            self.db.rollback()
            print "Database Error"
        
        self.disconnect()
        return r

    def getData(self,sql):
        self.connect()
        cursor=self.db.cursor()
        r=None
        try:
            cursor.execute(sql)
            rows=cursor.fetchall()
            r=[list(row) for row in rows]
            #r=rows

        except:
            print "Database Error"
        
        self.disconnect()
        return r

