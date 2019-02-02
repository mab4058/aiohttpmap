# Aiohttpmap

Bulk asynchronous processing of URLs.

## Example


```python
from aiohttpmap import AiohttpMap

urls = ['https://api.-placeholder-.com/endpoint']*10
results = AiohttpMap().map(urls, request_type='get')
```


## Example with authentication header.

```python
from aiohttpmap import AiohttpMap

urls = ['https://api.-placeholder-.com/endpoint']*10
auth_header = {'Authorization': 'token...'}
results = AiohttpMap().map(urls, request_type='get', headers=auth_header)
```
