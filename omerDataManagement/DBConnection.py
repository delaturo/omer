import yaml
import os.path
import mariadb
import BetterConsoleLog.Log as Log


GET_TOTAL_CHARSET = "select count('index') as totalChars from `character` c "
GET_TOTAL_CAPTURES = "select count('index') as totalChars from `capture` c "
GET_CATPURE = "select * from capture c order by 'index' desc"

class DBConnection:

    connectionInfo = None
    connection = None

    def __init__(self, connectionName = 'prd'):
        my_path = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(my_path, "connection.yaml")) as config:
            connections = yaml.full_load(config)
            conn = connections.keys()
            if connectionName in conn:
                Log.log("Getting connection information....." + connectionName)
                self.connectionInfo = connections[connectionName]
                Log.log("\tHost:" + self.connectionInfo['host'])
                Log.log("\tPort:" + str(self.connectionInfo['port']))
                Log.log("\tDB:" + self.connectionInfo['db'])
            else:
                Log.log("\tPConnection information not found....." + connectionName, logStyle=Log.style.RED)

    def connect(self):
        if not self.connection:
            Log.log("Connecting....")
            try:
                self.connection = mariadb.connect(
                    user=self.connectionInfo['usr'],
                    password=self.connectionInfo['pswd'],
                    host=self.connectionInfo['host'],
                    port=self.connectionInfo['port'],
                    database=self.connectionInfo['db']
                )
                Log.log("Connected.", logStyle=Log.style.GREEN)
            except mariadb.Error as e:
                Log.log(f"\tError connecting to MariaDB Platform: {e}", logStyle=Log.style.RED)
        return self.connection
    
    def close(self):
        if self.connection:
            self.connection.close()
        Log.log("Connection closed") 

    def getAllData(self,query):
        data = None
        if not self.connection:
            self.connection = self.connect()
        try: 
            cur = self.connection.cursor()
            cur.execute(query) 
            data = cur.fetchall()
        except mariadb.Error as e: 
            Log.log(f"Error: {e}", logStyle=Log.style.RED)
        return data

    def getData(self, query, offset, buffer):
        data = None
        if not self.connection:
            self.connection = self.connect()
        try: 
            cur = self.connection.cursor()
            cur.execute(query+" LIMIT "+str(offset)+","+str(buffer)) 
            data = cur.fetchall()
        except mariadb.Error as e: 
            Log.log(f"Error: {e}", logStyle=Log.style.RED)
        return data