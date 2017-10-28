#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
import os

print( "Content-type: text/plain\n")

if "HTTP_COOKIE" in os.environ:
    print( os.environ["HTTP_COOKIE"])
else:
    print( "HTTP_COOKIE not set!")