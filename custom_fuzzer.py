import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-w","--wordlist", help="wordlist to fuzz with")
args = parser.parse_args()

url="http://prd.m.rendering-api.interface.htb/vendor/dompdf/"

with open(f'{args.wordlist}', 'r') as f:
	for words in f:
		word = words.strip()
		url_fuzz = f'{url}{word}'
		r = requests.get(url_fuzz)
		sys.stdout.write(f'\r[+] {url_fuzz}')
		if "File not found." in r.text or "Access denied." in r.text:
			print(f'URL : {url_fuzz} \r {r.text}')