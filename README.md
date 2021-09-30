# Proxy Checker
[![Downloads](https://pepy.tech/badge/proxy-checking)](https://pepy.tech/project/proxy-checking)<br>A checker designed in Python 3.7 for checking proxy.<br>
If you need proxies, you can use this script [Proxy Grabber](https://github.com/iterweb/proxy_grabber)
## Description
This script takes a proxy as string input and tries to get data such as: 
- type (HTTP, SOCKS4, SOCKS5)
- time response (in seconds)
- anonymity (Anonymous or Transparent)
- country
- city
- country code
## Installation
```console
pip install proxy-checking
```
## Usage
```python3
from proxy_checking import ProxyChecker

checker = ProxyChecker()
r = checker.check_proxy('<ip>:<port>')
print(r)
```
if proxy is valid, will be return dictionary
```
{
  "status": True,
  "type": ["socks4", "socks5"],
  "time_response": "0.545",
  "anonymity": "Anonymous",
  "country": "Germany",
  "city": "Falkenstein",
  "country_code": "DE"
}
```
if proxy is not valid
```
{
  "status": False
}
```
## License
[MIT](LICENSE.md)
