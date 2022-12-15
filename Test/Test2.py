import subprocess
import copy
import re

def Blind() -> list[str, bool]:
    output = subprocess.check_output('ping -n 1 8.8.8.48')
    output = str(output.decode('cp866'))
    output= copy.copy("%r" % output)
    Routput = output.replace(r"\r\n", ",")
    Routput = Routput.split(",")
    Packet_loss_percentage=re"...% потерь"



    return "Мы подключены к мировой сетке"

if __name__ == "__main__":
    Blind()
