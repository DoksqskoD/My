import subprocess
import copy
def ping(*Hosting:str) -> str:
    if len(Hosting) == 0:
        Hosting:str="8.8.8.8"
    elif type(Hosting) == tuple:
        Hosting=Hosting[0]
    else:
        return "Ошибка в модуле ping, проверка значения по умолчанию"
    Survey=subprocess.check_output("powershell ping " + Hosting)
    Survey=copy.deepcopy(Survey.strip().decode('cp866'))
    Survey=Survey.split("""\r\n""")
    if Survey[8]=='    (0% потерь)':
        return "Мы подключены к мировой сетке"
    elif Survey==1:
        return "Мировая сеть не доступна или много потерянных пакетов"
    else:
        return "Ошибка в модуле ping, проверка выходных данных из CMD"