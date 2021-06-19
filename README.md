[![Build Status](https://travis-ci.com/shreyanshu7101904/notix-push-notification.svg?branch=main)](https://travis-ci.com/shreyanshu7101904/notix-push-notification) [![Code Grade](https://www.code-inspector.com/project/23881/status/svg)](https://frontend.code-inspector.com/project/23881/dashboard) [![Coverage Status](https://coveralls.io/repos/github/shreyanshu7101904/notix-push-notification/badge.svg?branch=main)](https://coveralls.io/github/shreyanshu7101904/notix-push-notification?branch=main) [![Documentation Status](https://readthedocs.org/projects/notix-python/badge/?version=latest)](https://notix-python.readthedocs.io/en/latest/?badge=latest)
# notix-python
Notix Push Notiication Wrapper
## Installation
Use pip to install latest package from PyPI.
``` 
pip install notix-python-wrapper
```
## Usage
To use this package
```python

from notix.notix_api import Notix

app_id = "Your Notix App Id"

token = "Your API token"

notix_object = Notix(app_id, token)

message = { 

    "message": {
    
    "title": "test Notification", 
    
    "text":"sample notifiaction text"
    
    }}
    
resp = notix_object.send_notification(message)

print(resp)
```

## Documentation
For full documentation check [Here](https://notix-python.readthedocs.io) 
