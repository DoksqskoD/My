import subprocess
import json

def Module_firewall():

    runningProcesses = subprocess.check_output("powershell Get-NetFirewallProfile -Name Public | ConvertTo-Json")
    runningProcesses=json.loads(runningProcesses)
    for x in runningProcesses:
            print(x)
            print(runningProcesses[x])

Module_firewall()