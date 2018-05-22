from django.http import HttpResponse
import pyodbc 

def index(request):
    server = 'tcp:edisga-server.database.windows.net' 
    database = 'edisga-sql' 
    username = '*************' 
    password = '**********' 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    #Sample select query
    cursor.execute("SELECT * FROM SalesLT.Product") 
    row = cursor.fetchone()
    print(row)          # access by column index (zero-based)
    return HttpResponse(row)