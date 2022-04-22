#!C:\Users\Onyedikachi Amugo\AppData\Local\Programs\Python\Python310\python.exe
import cgi
from datetime import date
import random
import cgitb      #use for error traces
cgitb.enable()    #use for error traces


# Create instance of FieldStorage 

form = cgi.FieldStorage() 


# Get data from fields  

name = form.getvalue('name')        # name of the field is same as in client form

Email = form.getvalue('Email')
ticket1 = form.getvalue('ticket1') 
ticket2 = form.getvalue('ticket2') 
ticket1= int (ticket1)
ticket2= int (ticket2)
ticket= ticket1 + ticket2
for x in range(1):

   Booking_number=(random.randint(2,10000))

if form.getvalue('route'):

   route = form.getvalue('route')

else:

   route = "Not entered"


if form.getvalue('payment'):

    Payment_Method = form.getvalue('payment')

else:

   Payment_Method = "Not entered"


Booking_date = date.today().strftime('%d-%m-%Y')







print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")

print("<title>ST FORM </title>")

print("</head>")

print("<body>")

print("<h1>THANK YOU FOR BOOKING AT SKY TRAVEL, HERE ARE YOUR DETAILS:</h1>")

print("<br>")

print("<h2> BOOKING DETAILS :</h2>")

print("<h3>Booking number: ST.BUS #%s</h3>" % (Booking_number))

print("<h3>Booking date: %s</h3>" % (Booking_date))

print("<h3>Name: %s </h3>" % (name))

print("<h3>Email: %s </h3>" % (Email))

print ("<h3> Route: %s</h3>" % (route))
print("<br>")

print("<h2> PAYMENT DETAILS :</h2>")

print("<h3>Item(s): %s x Sky Travel Bus tickets  <br>  (Adults:%s , Children:%s    )</h3>"%(ticket,ticket1, ticket2))   

print("<h3>Payment Method:  %s</h3>" % (Payment_Method))

print("<h3>Subtotal :</h3>" )

print("<h3>Discount:</h3>" )
print("<h3>Total :</h3>" )

print("</body>")

print("</html>")



import mysql.connector
from mysql.connector import Error



def connect():

    try:

       conn = mysql.connector.connect(host='localhost',
                                        database='st_portal',

                                        user='root',

                                        password='')
                                        

       if conn.is_connected():

         if "Submit" in form:

            name = form.getvalue('name')        # name of the field is same as in client form
            Email = form.getvalue('Email')
            ticket1 = form.getvalue('ticket1') 
            ticket2 = form.getvalue('ticket2') 
            ticket1= int (ticket1)
            ticket2= int (ticket2)
            ticket= ticket1 + ticket2
            for x in range(1):
               Booking_number=(random.randint(2,10000))

            if form.getvalue('route'):
               route = form.getvalue('route')
            else:
               route = "Not entered"

            if form.getvalue('payment'):
              Payment_Method = form.getvalue('payment')
            else:
               Payment_Method = "Not entered"


            Booking_date= date.today().strftime('%d-%m-%Y')


        
         cursor = conn.cursor()
         query = "INSERT INTO bus (Booking_number, Name, Email, Route, Payment_Method, Booking_date, Item) VALUES (%s, %s,%s, %s,%s,%s, %s)"
         args = (Booking_number, name, Email, route, Payment_Method, Booking_date,ticket)
         cursor.execute(query, args)
         html = """
         """.format(

                    Booking_number=Booking_number,

                    name=name,

                    Email=Email,

                    route=route,

                    Payment_Method=Payment_Method,

                    Booking_date=Booking_date,

                    ticket=ticket
                    )
         print(html)

         conn.commit()
         cursor.close()


       

    except Error as e:
        print(e)
    

    finally:
        conn.close()


if __name__ == '__main__':
    connect()