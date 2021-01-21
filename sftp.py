import pysftp

srv = pysftp.Connection(host="www.destination.com", username="dewa",
password="root123!",log="./temp/pysftp.log")

with srv.cd('public'): #chdir to public
    srv.put('') #upload file to nodejs/

# Closes the connection
srv.close()