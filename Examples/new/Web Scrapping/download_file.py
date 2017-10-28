#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python


import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print(res.text[:250])