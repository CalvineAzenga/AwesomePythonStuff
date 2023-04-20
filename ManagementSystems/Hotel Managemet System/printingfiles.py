import subprocess

# get Printer names
data = subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\r\r\n')
data = data[1:]
i = 0
for line in data:
    for printer_name in line.split('  '):
        if printer_name != "":
            print(printer_name)
            i += 1
            break
print(f"A total of {i} printers installed")
