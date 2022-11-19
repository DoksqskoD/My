
import os
_PID = ('tasklist /FO CSV').split('\n')
result = os.popen(_PID[0]).read()
print(result)
