import subprocess
import json

output = subprocess.check_output('pip list --format=json')

output=json.loads(output)
for i in output:
    print(i["name"])
    out=subprocess.check_output("pip install "+i["name"]+" -U")
    print(out)

print(output)
