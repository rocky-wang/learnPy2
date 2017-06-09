# ^_^ coding: utf-8
import json
import requests

BASE_URL = 'https://api.github.com'


def build_url(endpoint):
    return '/'.join([BASE_URL, endpoint])


def better_print(data):
    return json.dumps(json.loads(data), indent=4)


def get_method(builded_url):
    response = requests.get(builded_url, auth=('imoocdemo', 'imoocdemo123'))
    # print response.text
    print better_print(response.text)
    # data1 = json.loads(response.text)
    # print json.loads(response.text)['name']


def json_method(builded_url):
    response = requests.post(builded_url, auth=('rocky-wang', 'aishila112'), json={'company': 'changhong'})
    print response.request.body
    print response.status_code

if __name__ == '__main__':
    # u1 = build_url('users/rocky-wang')
    # u1 = build_url('user/emails')
    u1 = build_url('user')
    print u1
    json_method(u1)

