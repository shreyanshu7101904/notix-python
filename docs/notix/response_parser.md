Title: Notix Python Wrapper
Author: Shreyanshu Shankar
Date: 2021-06-21

# Class `notix.notix_api.ResponseParser`
Intakes `requests.Response` Objects and returns formatted response.
# Methods Available
### Str representation of requests object 
!!! note "notix.notix_api.ResponseParser.__str__"
        * `__str__` string representation of response object
            * `parameters` None
            * `returns` - str Response of your requests


### Response Parser
!!! note "notix.notix_api.ResponseParser.parse"
        * `parse` Parse Response
            * `parameters` - None
            * `returns` - dict object with two parameters `status_code` and `message`.
