# Proxy Checker
A checker designed in Python 3 for checking proxy.
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
checker.check_proxy('<ip>:<port>')
```
if proxy is valid, will be return dictionary
```json
{
  "status": 1,
  "type": ["socks4", "socks5"],
  "time_response": "0.545",
  "anonymity": "Anonymous",
  "country": "Germany",
  "city": "Falkenstein",
  "country_code": "DE"
}
```
if proxy is not valid
```json
{
  "status": 0
}
```
## License
[MIT](LICENSE.md)