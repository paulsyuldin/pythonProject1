import requests
import pytest

url = 'http://app02-qa-01.prod01ru.sptlab.net:14080'

request = requests.post(url=f'{url}/api/mcdn/token/check',
                        headers={
                            "accept": "application/json",
                            "clientToken": "99f7cdf8-c13c-46b9-a4eb-b909b3655688"
                        })

print(request.json(), request.status_code)
