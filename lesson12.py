import subprocess

result = subprocess.run(["ls"], capture_output=True, text=True)
print(result.stdout)

result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)
print(result.returncode)


import subprocess

def check_device(ip):
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True)
    if result.returncode == 0:
        return "Device OK"
    else:
        return "No response"

devices = ["8.8.8.8", "192.0.2.1"]

for ip in devices:
    status = check_device(ip)
    print(status, "-", ip)


