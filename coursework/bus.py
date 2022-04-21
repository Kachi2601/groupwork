#!C:\Users\Onyedikachi Amugo\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import random
import cgitb      #use for error traces
cgitb.enable()    #use for error traces

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields  
name = form.getvalue('name')        # name of the field is same as in client form
Email = form.getvalue('Email') 
for x in range(1):
    ran=(random.randint(2,10000))
if form.getvalue('route'):
   route = form.getvalue('route')
else:
   route = "Not entered"





print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>ST FORM </title>")
print("</head>")
print("<body>")
print("<h1> BOOKING DETAILS :</h2>")
print("<h2>Booking number: ST.BUS #%s</h2>" % (ran))
print("<h2>Name: %s </h2>" % (name))
print("<h2>Email: %s </h2>" % (Email))
print ("<h2> Route: %s</h2>" % (route))
print("<h2>Payment Method:</h2>" )
print("<h2>Discounts:</h2>" )
print("</body>")
print("</html>")