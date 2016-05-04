import requests
import argparse


parser = argparse.ArgumentParser(description='Return information on UO people.')
parser.add_argument('-n', '--name', nargs='+', help="a name")
parser.add_argument('-e', '--email', nargs='+', help="an email address")
parser.add_argument('-s', '--email', help="an email address")
args = parser.parse_args()

payload = { 'm':"staff", 'd':"person", 'p':"findpeople/find_results"}
if args.name:
    payload['s'] = args.name
    payload['b'] = "name"
elif args.email:
    payload['s'] = args.email
    payload['b'] = "email"

    

URL = 'http://directory.uoregon.edu/ws-directory-client/directory.jsp'
session = requests.session()
r = requests.post(URL, data=payload)
print(r.text)

