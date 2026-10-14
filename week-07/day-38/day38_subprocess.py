import subprocess

result = subprocess.run(["Powershell","-command", "Get -Date"], capture_output = True, text = True )

print(result.stdout)