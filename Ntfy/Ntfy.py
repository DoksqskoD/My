import requests
from time import sleep
from Screen_resolution import Screen
import Blind

def main():
    Triger=0
    while True:

        Array=list(Blind.Blind())
        sleep(1)
        Tim_Array=list(Blind.Blind())

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
        if Triger == 100:
            print(Screen("Skrin"))
            requests.post("https://ntfy.sh/MyPCJ9rV9Tn20Y1UkzNQrChPFG4ho2RE2AqPkZMeTZ5y",
                          data=open(r"D:\KPython\Ntfy\Skrin.png", 'rb'),
                          headers={"Filename": "Skrin.png"})
            Triger=0
        Triger+=1
if __name__ == "__main__":
    main()