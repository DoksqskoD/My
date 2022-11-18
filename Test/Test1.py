import subprocess
import copy

output = subprocess.check_output('tasklist /fo csv /nh')
output = str(output.decode('cp866'))
Routput = copy.copy("%r" % output)
del output
Routput=Routput.replace(r"\r\n", ",")
Routput=Routput.split(",")
Routput=Routput[::5]
del Routput[len(Routput)-1]
