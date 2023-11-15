import subprocess

command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        ssid = i
        password = results[0]
        print("Wifi SSID: {}\n   Wifi Password: {}\n-------------------------------------------------------------".format(ssid, password))
    except IndexError:
        ssid = i
        password = ""
        print("Wifi SSID: {}\n   Wifi Password: {}\n-------------------------------------------------------------".format(ssid, password))

input("")

