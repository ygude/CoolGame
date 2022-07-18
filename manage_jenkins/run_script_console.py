import requests

with open('create_creds.groovy', 'r') as fd:
    data = fd.read()
#r = requests.post('http://127.0.0.1:9999/scriptText', auth=('username', 'api-token'), data={'script': data})
r = requests.post('http://127.0.0.1:9999/scriptText', auth=('admin', 'admin'), data={'script': data})
print(r)
