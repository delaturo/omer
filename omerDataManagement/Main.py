import os
import DBConnection
import ImgProcessor
import BetterConsoleLog.Log as Log
from datetime import datetime


def saveData(data,dataFolder):
    if not dataFolder:
        my_path = os.path.abspath(os.path.dirname(__file__))
        dataFolder = os.path.join(my_path,"..\\captures_"+datetime.now().strftime("%d-%m-%Y_%H%M%S"))
    if not os.path.exists(dataFolder):
        os.mkdir(dataFolder)
    for d in data:
        dFolder = os.path.join(dataFolder,str(d[1]))
        if not os.path.exists(dFolder):
            os.mkdir(dFolder)
        dFile = os.path.join(dFolder,str(d[0])+".jpg")
        tempFile = ImgProcessor.getTempFile()
        with open(tempFile, 'wb') as f:
            f.write(d[2])
        ImgProcessor.removeAlpha(tempFile,dFile)
        os.remove(tempFile)
    return dataFolder



Log.log("========= Connecting to DB =========", logStyle=Log.style.BOLD)
dbConn = DBConnection.DBConnection("prd")

data = dbConn.getAllData(DBConnection.GET_TOTAL_CHARSET)
if (data):
    Log.log("# Chars : " + str(data[0][0]))

data = dbConn.getAllData(DBConnection.GET_TOTAL_CAPTURES)
if (data):
    Log.log("# Captures : " + str(data[0][0]))
    totalCaptures = data[0][0]

# Gets the catpures from the DB
index = 0
bufferSize = 10
dataFolder = None
Log.log("Retrieving data:")

while (index < totalCaptures):
    Log.logAsProgress("\tProgress: " + str(index) + " / " + str(totalCaptures), progress=(index/totalCaptures))
    data = dbConn.getData(DBConnection.GET_CATPURE,index,bufferSize)
    dataFolder = saveData(data,dataFolder)
    index += len(   data)
Log.logAsProgress("\tProgress: " + str(index) + " / " + str(totalCaptures), progress=(index/totalCaptures))
dbConn.close()

Log.log("Standaring images:")
ImgProcessor.cropImagesIteration(dataFolder)
Log.log("... Done")


Log.log("########## FINISHED! ##########", logStyle=Log.style.GREEN)