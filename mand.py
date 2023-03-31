import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from mand import ajbuy
    ajbuy()
elif bit == '32bit':
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')