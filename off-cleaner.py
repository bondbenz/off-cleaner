import requests
import time
print '''
[offline sites cleaner]
[code by bondbenz - twin.ninja]
'''
sites = raw_input("Enter Your List of Sites : ")
bond = open(sites,'r').readlines()
for benz in bond:
    site = benz.rstrip()
    headers = {'foobar': 'raboof'}
    try:
        r = requests.get(site, headers=headers)
        if r.status_code == 200:
            with open('clean.txt', 'a') as myfile:
                myfile.write(site)
                myfile.write('\n')
            print site+' [200 | ok]'
            time.sleep(0.5)
    except:
        pass
