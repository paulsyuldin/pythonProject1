import requests
url = 'http://app02-qa-01.prod01ru.sptlab.net:14080'
request_1 = requests.post(url=f'{url}/api/mcdn/token/check',
                            headers={
                                "accept": "application/json",
                                "clientToken": "99f7cdf8-c13c-46b9-a4eb-b909b3655688"
                            })

request_2 = requests.get(url=f'{url}/api/mcdn/ping',
                           headers={
                               "accept": "application/json",
                               "clientToken": "99f7cdf8-c13c-46b9-a4eb-b909b3655688"
                           })

request_3 = requests.get(url=f'{url}/api/mcdn/order/status',
                           headers={
                               "accept": "application/json",
                               "clientToken": "99f7cdf8-c13c-46b9-a4eb-b909b3655688",
                               "orderId": "f6d8dbd1-2bee-47e5-94e9-897be6a0f9c1"
                           })