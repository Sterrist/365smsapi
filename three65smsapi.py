import requests

class three65sms:
    def __init__(self, api_key):
        self.api_key = api_key

    def getnumbersstatus(self, country, operator):
        params = {
            'api_key': self.api_key,
            'action': 'getNumbersStatus',
            'country': country,
            'operator': operator
        }
        request = requests.get(url='https://365sms.ru/stubs/handler_api.php', params=params)
        return request.json()

    def getbalance(self):
        params = {
            'api_key': self.api_key,
            'action': 'getBalance'
        }
        request = requests.get(url='https://365sms.ru/stubs/handler_api.php', params=params)
        return request.text

    def buynumber(self, service, country, operator):
        params = {
            'api_key': self.api_key,
            'action': 'getNumber',
            'country': country,
            'operator': operator,
            'service': service
        }
        request = requests.get(url='https://365sms.ru/stubs/handler_api.php', params=params)
        return request.text

    def setnumberstatus(self, id, status):
        params = {
            'api_key': self.api_key,
            'action': 'setStatus',
            'id': id,
            'status': status
        }
        request = requests.get(url='https://365sms.ru/stubs/handler_api.php', params=params)
        return request.text

    def getnumberstatus(self, id):
        params = {
            'api_key': self.api_key,
            'action': 'getStatus',
            'id': id
        }
        request = requests.get(url='https://365sms.ru/stubs/handler_api.php', params=params)
        return request.text

    def getallprices(self, service, country):
        params = {
            'api_key': self.api_key,
            'action': 'getPrices',
            'country': country,
            'service': service
        }
        request = requests.get(url='https://365sms.ru/stubs/handler_api.php', params=params)
        return request.json()