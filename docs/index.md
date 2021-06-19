Title: Notix Python Wrapper
Author: Shreyanshu Shankar
Date: 2021-06-21

# Welcome Notix Python Wrapper Package 
## [![Build Status](https://travis-ci.com/shreyanshu7101904/notix-push-notification.svg?branch=main)](https://travis-ci.com/shreyanshu7101904/notix-push-notification) [![Code Grade](https://www.code-inspector.com/project/23881/status/svg)](https://frontend.code-inspector.com/project/23881/dashboard) [![Coverage Status](https://coveralls.io/repos/github/shreyanshu7101904/notix-push-notification/badge.svg?branch=main)](https://coveralls.io/github/shreyanshu7101904/notix-push-notification?branch=main)
A python wrapper for [Notix](https://notix.co/) **Push Notification**.

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

print(response)
```
!!! Note
    To get **app_id** and **token** kindly visit on [Notix](https://notix.co) add your website.
    
    Create your api token [here](https://app.notix.co/auth/apiAccess).

* `message` - Message Contents **type dict**.
    * `icon` - Url of small image displayed in Push Notification **type str**.
    * `image` - Url of image displayed in push message **type str**.
    * `text` - Additional test message **type str**.  
    * `title` - Message title **type str**.  
    * `url` - Target Url where users will be redirected on click **type str**.
* `limit` - Maximum recipient amount **type int** Example 10.
* `schedule` - Schedule content **type dict**.
    * `interval` - Mailing repeat interval in minutes, minimum 60 maximum 43200(30 days) **type int**.
    * `start_date` - Date and time when notification will be sent format _YYYY-MM-DD hh:mm:ss_ in UTC **type str**.
* `scheduled_date` - Scheduling date **type str**.
* `ttl` - Time to Live in minutes **type int**.

!!! Note
    For core api parameters you can visit [here](https://docs.notix.co/api-send.html) 
