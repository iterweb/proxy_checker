import requests
import random
from time import time

user_agent = [
    'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20060814 Firefox/51.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43',
]
headers = {
        'User-Agent': random.choice(user_agent),
    }


class ProxyChecker:

    def __init__(self):
        self.ip = self.get_my_ip()

    def get_my_ip(self):
        sites = ['http://ipinfo.io/ip', 'https://api.ipify.org/', 'http://ifconfig.io/ip']
        ip = self.get_info(url=random.choice(sites))
        return ip.text

    def get_info(self, url=None, proxy=None):
        info = {}
        proxy_type = []
        judges = ['http://proxyjudge.us/azenv.php', 'http://azenv.net/', 'http://httpheader.net/azenv.php', 'http://mojeip.net.pl/asdfa/azenv.php']
        if url != None:
            try:
                response = requests.get(url, headers=headers, timeout=5)
                return response
            except:
                pass
        elif proxy != None:

            for protocol in ['http', 'socks4', 'socks5']:
                proxy_dict = {
                    'https': f'{protocol}://{proxy}',
                    'http': f'{protocol}://{proxy}',
                }
                try:
                    start = time()
                    response = requests.get(random.choice(judges), proxies=proxy_dict, headers=headers, timeout=5)
                    finish = time() - start
                    if response.status_code == 200:
                        proxy_type.append(protocol)
                        info['type'] = proxy_type
                        info['time_response'] = ("%.3f" % finish)
                        info['status'] = True
                        if str(self.ip) in response.text:
                            info['anonymity'] = 'Transparent'
                        else:
                            info['anonymity'] = 'Anonymous'
                        if protocol == 'http':
                            return info
                except:
                    pass

            if 'status' not in info.keys():
                info['status'] = False
                return info
            else:
                return info

    def get_geo(self, ip):
        url = ['http://ipwhois.app/json/', 'http://ip-api.com/json/', 'https://api.techniknews.net/ipgeo/']
        resp = self.get_info(url=f'{random.choice(url)}{ip}')
        return resp

    def check_proxy(self, proxy):
        ip = proxy.split(':')
        resp = self.get_info(proxy=proxy)

        if resp['status'] == True:
            result = {}
            geo = self.get_geo(ip[0])
            geo_info = geo.json()
            result['status'] = resp['status']
            result['type'] = resp['type']
            result['time_response'] = resp['time_response']
            result['anonymity'] = resp['anonymity']
            result['country'] = geo_info['country']
            result['city'] = geo_info['city']
            try:
                result['country_code'] = geo_info['country_code']
            except:
                result['country_code'] = geo_info['countryCode']

            return result

        else:
            return resp
