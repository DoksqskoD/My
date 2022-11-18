import requests
from time import sleep
from Screen_resolution import Screen
import shutil
import Blind

def main():
    Triger=0
    while True:

        Array=Blind.Blind()
        sleep(2)
        Tim_Array=Blind.Blind()
        if len(Array) != len(Tim_Array):
            if len(Array) < len(Tim_Array):
                for X in Tim_Array:
                    if Array.count(X) == 0 and Array.count(X) != Tim_Array.count(X):
                        requests.post("https://ntfy.sh/MyPCJ9rV9Tn20Y1UkzNQrChPFG4ho2RE2AqPkZMeTZ5y", data=("Программа "+ X +" запущена").encode(encoding='utf-8'))
                        break
            elif len(Array) > len(Tim_Array):
                for X in Array:
                    if Tim_Array.count(X) == 0 and Array.count(X) != Tim_Array.count(X):
                        requests.post("https://ntfy.sh/MyPCJ9rV9Tn20Y1UkzNQrChPFG4ho2RE2AqPkZMeTZ5y", data=("Программа "+ X +" выключена").encode(encoding='utf-8'))
                        break
        if Triger == 1:
            Screen("Skrin")
            requests.post("https://ntfy.sh/MyPCJ9rV9Tn20Y1UkzNQrChPFG4ho2RE2AqPkZMeTZ5y",
                          data=open("D:\KPython\Skrin.png", 'rb'),
                          headers={ "Filename": "Skrin.png" })
            shutil.rmtree("D:\KPython\Skrin.png")
            Triger=0
        Triger+=1
if __name__ == "__main__":
    main()