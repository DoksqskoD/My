import requests
from Ntfy.Screen_resolution import Screen

if True:
    print(Screen("Skrin"))
    requests.post("https://ntfy.sh/MyPCJ9rV9Tn20Y1UkzNQrChPFG4ho2RE2AqPkZMeTZ5y",
                  data=open("d:\KPython\Test\Skrin.png", 'rb'),
                  headers={"Filename": "Skrin.png"})