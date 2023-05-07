#!/usr/bin/env python
import cgi, os

form = cgi.FieldStorage()

# Get filename of uploaded image
fileitem = form['image-file']
if fileitem.filename:
    filename = os.path.basename(fileitem.filename)
    with open(filename, 'wb') as f:
        f.write(fileitem.file.read())
    print(filename)
else:
    print('No file uploaded')
