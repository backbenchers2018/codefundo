#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()

fname = form.getvalue('firstname')
lname = form.getvalue('lastname')
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello CGI 2ND</title>")
print("</head>")
print("<body>")
print("<h2>Hello {} {}</h2>".format(fname,lname))
print("</body>")
print("</html>")
