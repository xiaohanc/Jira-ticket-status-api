import requests
import os
user = os.environ['JIRA_USER']
password = os.environ['JIRA_TOKEN']
headers = {
    'Content-Type': 'application/json',
}

params = (
    ('expand', 'transitions.fields'),
)

data = '{"transition":{"id":"11"}}'

url = 'https://viceqa.atlassian.net/rest/api/latest/issue/CMS-5/transitions'

response = requests.post(url, headers=headers, params=params, data=data, auth=(user, password))
