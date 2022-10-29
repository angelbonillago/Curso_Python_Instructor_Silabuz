import requests

resp = requests.get("https://ivantay2003.medium.com/http-status-code-1e69e3d579c1") #haciendo una peticion



print(resp)
print(type(resp.status_code))

if(resp.status_code==200):
    print('PAGINA OK')
