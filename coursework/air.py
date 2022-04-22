import cgi 
import cgitb
cgitb.enable()

import mysql.connector
from mysql.connector import Error

form = cgi.FieldStorage()

name = form.getvalue('Name')
mail = form.getvalue('Email')
ticket1 = int(form.getvalue('ticket1'))
ticket2 = int(form.getvalue('ticket2'))
ticket = ticket1 + ticket2

for x in range(1):
    Booking_number=(random.randint(2,10000))

if form.getvalue('Choose Depart-Destination'):
    route = form.getvalue('Choose Depart-Destination')
else:
    route = "Invalid Route !!!\n Please Refer To The Provided List"

if form.getvalue("Choose Payment"):
    Payment_Method = form.getvalue('Choose Payment Method')
else:
    route = "Invalid Choice"

booking_date = date.today().strftime('%d-%m-%Y')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>THANK YOU FOR BOOKING AT SKY TRAVEL. HERE IS YOUR AIR TRAVEL INFORMATION</title>")
print("</head>")
print("<body>")
print("<h1>PERSONAL INFORMATION</h1>")
print("<h2>Booking number: ST.PLANE #%s</h2>" % (Booking_number))
print("<h2>Booking date: %s</h2>" % (booking_date))
print("<h2> Name: %s</h2>" %(name))
print("<h2> Email Address: %s </h2>" %(mail))
print("<h2> Selected Travel Route: %s </h2>" % (route))
print("<br><br>")
print("<h1> PAYMENT INFROMATION </h1>")
print("<h2>Item(s): %s x Sky Travel Bus tickets  <br>  (Adults:%s , Children:%s    )</h2>"%(ticket,ticket1, ticket2))   
print("<h2>Payment Method:  %s</h2>" % (Payment_Method))
print("<h2>Subtotal :</h2>" )
print("<h2>Discount:</h2>" )
print("<h2>Total :</h2>" )
print("</body>")
print("</html>")


def Connect():
    try: 
        con = mysql.connector.connect(host='localhost', database='st_portal', user='root', password='')
        
        if con.is_connected():
            if "Submit" in form:
                name = form.getvalue('Name')
                mail = form.getvalue('Email')
                ticket1 = int(form.getvalue('ticket1'))
                ticket2 = int(form.getvalue('ticket2'))
                ticket = ticket1 + ticket2

                for x in range(1):
                    Booking_number=(random.randint(2,10000))

                if form.getvalue('Choose Depart-Destination'):
                    route = form.getvalue('Choose Depart-Destination')
                else:
                    route = "Invalid Route !!!\n Please Refer To The Provided List"

                if form.getvalue("Choose Payment"):
                    Payment_Method = form.getvalue('Choose Payment Method')
                else:
                    Payment_Method = "Invalid Choice"

                booking_date = date.today().strftime('%d-%m-%Y')
                
                print("Connnection Successful")
                cursor = con.cursor()
                query = "INSERT INTO bus (Booking_number, Name, Email, Route, Payment_Method, Booking_date, Item) VALUES (%s, %s,%s, %s,%s,%s, %s)"
                args = (Booking_number,name,mail,route,Payment_Method,booking_date,ticket)
                cursor.execute = (query,args)

                html = """
                <body> 
                <h1> HELLO {name}.\n YOUR EMAIL ADDRESS IS : {mail}.\n YOUR DESIRED TRAVEL ROUTE IS: {route}.\n\n THANK FOR SELECTING TO TRAVLE WITH US. </h1>
                </body>
                """.format(
                    Booking_number=Booking_number,name=name, mail=mail,route=route,Payment_Method=Payment_Method,booking_date=booking_date,ticket=ticket
                )
                print(html)
                con.commit()
                cursor.close()

        else:
            print("Invalid!!")
    except Error as e:
        print(e)

    finally:
        con.close()


if __name__ == '__main__':
    connect()


                    
