#somu 07-02-2018
#Reference: https://automatetheboringstuff.com/chapter11/


import webbrowser, sys, pyperclip
print (sys.argv)
if len(sys.argv) > 1:
    # Get address from command line.
  address = ' '.join(sys.argv[1:])
  print (address)
else:
  address = pyperclip.paste()

#webbrowser.open('https://google.com/maps/place/'+ address)

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
if res.status_code == requests.codes.ok:
    len(res.text)
    print(res.text[:250])

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print('There was a problem: %s' % (exc)) 
    
#TODO: Get address from clipboard.