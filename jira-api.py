import requests
import os
user = os.environ['JIRA_USER']
password = os.environ['JIRA_TOKEN']
domain_name = os.environ['domain']
issue_name = os.environ['issue_name']

headers = {
    'Content-Type': 'application/json',
}

params = (
    ('expand', 'transitions.fields'),
)

data = '{"transition":{"id":"11"}}'

url = 'https://' + domain_name + '.net/rest/api/latest/issue/' + issue_name +'/transitions'

response = requests.post(url, headers=headers, params=params, data=data, auth=(user, password))
