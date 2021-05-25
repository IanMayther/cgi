#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
listval = form.getlist('operand')
total = 0

try:
    for item in listval:
        total += int(item)
except ValueError:
    total = 0

print("Content-type: text/plain")
print()
print(str(total))
