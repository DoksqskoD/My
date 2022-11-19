import subprocess
import copy

def Blind():
    output = subprocess.check_output('tasklist /fo csv /nh')
    output = str(output.decode('cp866'))
    Routput = copy.copy("%r" % output)
    del output
    Routput = Routput.replace(r"\r\n", ",")
    Routput = Routput.split(",")
    Routput = Routput[::5]
    del Routput[len(Routput) - 1]
    return set(Routput)
if __name__ == "__main__":

    Blind()

