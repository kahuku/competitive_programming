import requests

URL = 'https://api.simplenexus.com/group_profiles/json/c7598ae3-64c4-4e8e-b625-c73e68444640/loanofficers.json'

def get_and_parse():
    response = requests.get(URL).json()['loanOfficers']
    d = {response[i]['sid']: response[i] for i in range(len(response))}
    for key in d.keys():
        print(str(key) + ":" + d[key]['name'] + " : " + d[key]['city'])

get_and_parse()