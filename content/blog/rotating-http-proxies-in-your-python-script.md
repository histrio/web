---
title: "Rotating HTTP proxies in your python script"
date: 2022-11-11 17:15:36.459511557+00:00
canonical: https://gem.org.ru/rotating-http-proxies-in-your-python-script
---
 Ok,  there can be a whole bunch of reasons why you would need to use multiple proxy servers at once. But most of them, to be honest, are related to playing around with bot detection, scrapping, and other not-so-honorable stuff.

<!--more-->

Anyway. We have a task to get https://httpbin.org/ip content and to be sure that each time I will get a result that differs from the previous one.
```python
import urllib.request
import json

previous = None
while True:
    with urllib.request.urlopen('https://httpbin.org/ip') as response:
        current = json.loads(response.read())['origin']
        assert previous != current, f"Got the same {current} twice in a row"
        print("OK: ", current)
        previous = current
```
That will obviously fail. The second request will get the same IP which is not OK for us. 
```bash
$ python script.py 
OK:  79.143.111.139
Traceback (most recent call last):
  File "script.py", line 8, in <module>
    assert previous != current, f"Got the same {current} twice in a row"
AssertionError: Got the same 79.143.111.139 twice in a row
```

Let's extend ProxyHandler a little bit. We need a way to define multiple proxies for one proto and circulate it for each request. A little trick with cycle iterator will do the thing

```python
import urllib.request
import json
import itertools

class RotatingProxyHandler(urllib.request.ProxyHandler):

    def __init__(self, proxies):
        self.proxies = proxies or {}
        for type, urls in self.proxies.items():
            type = type.lower()
            setattr(self, f'_{type}_proxies', itertools.cycle(urls))
            setattr(self, f'{type}_open',
                    lambda r, proxy=getattr(self, f"_{type}_proxies"), type=type, meth=self.proxy_open:
                        meth(r, proxy, type))

    def proxy_open(self, req, proxy, type):
        super().proxy_open(req, next(proxy), type)


proxy_support = RotatingProxyHandler(proxies={'https': [
    "92.205.22.114:38080",
    "169.57.1.85:8123",
]})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

previous = None
while True:
    with urllib.request.urlopen('https://httpbin.org/ip') as response:
        current = json.loads(response.read())['origin']
        assert previous != current, f"Got the same {current} twice in a row"
        print("OK: ", current)
        previous = current

```

And now we have it!

```bash
$ python script.py
OK:  92.205.22.114
OK:  169.57.1.85
OK:  92.205.22.114
OK:  169.57.1.85
OK:  92.205.22.114
OK:  169.57.1.85
OK:  92.205.22.114
``` 

 {{< public-inbox \>}}