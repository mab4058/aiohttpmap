[![PyPI](https://img.shields.io/pypi/v/aiohttpmap.svg?style=flat-square)](https://pypi.org/project/aiohttpmap/)

# Aiohttpmap

Bulk asynchronous processing of URLs using the aiohttp package.

## Installation

`pip install aiohttpmap`

## Example


```python
import asyncio
from aiohttpmap import AiohttpMap

urls = ['https://api.-placeholder-.com/endpoint']*10

loop = asyncio.get_event_loop()
try:
    results = loop.run_until_complete(AiohttpMap().map(urls, request_type='get'))
finally:
    loop.close()
```


## Example with authentication header.

```python
import asyncio
from aiohttpmap import AiohttpMap

urls = ['https://api.-placeholder-.com/endpoint']*10
auth_header = {'Authorization': 'token...'}

loop = asyncio.get_event_loop()
try:
    results = loop.run_until_complete(AiohttpMap().map(urls, request_type='get', headers=auth_header))
finally:
    loop.close()
```
