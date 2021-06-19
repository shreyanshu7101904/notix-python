# Welcome Notix Python Wrapper Package
A python wrapper for [Notix](https://notix.co/) **Push Notification**.

## Installation
Use pip to install latest package from PyPI.
``` 
pip install notix-python-wrapper
```
## Usage
To use this package
```

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
You can also customise more parameters for notifications.

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


## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
