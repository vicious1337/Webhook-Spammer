import requests

print('''/ vicious#1337
''')

url = input('Webhook URL: ')

msg = input('Message to spam: ')

data = {
    "content": msg
}

def send(f):
    r = requests.post(url, data=data)
    try:
        print('Succesfully sent')
    except:
        f += 1
    return f
f = 0
while True:
   f = send(f)
