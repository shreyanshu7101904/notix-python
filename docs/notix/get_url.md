Title: Notix Python Wrapper
Author: Shreyanshu Shankar
Date: 2021-06-21
# get_url `notix.notix_api.get_url`

Url builder function to create `Notix Api url` based on parameter

* `parameter`
    * `path_name`: url path string as defined in [constants](../../constants/constant/). Path name can be **send**, **audience_add** etc.
* `returns` - Notix Api url **type str**.
* `raises` - `UrlPathException` as defined in [exceptions](../../exceptions/exceptions/)
