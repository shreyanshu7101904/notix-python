Title: Notix Python Wrapper
Author: Shreyanshu Shankar
Date: 2021-06-21

# Notix Class `notix.notix_api.Notix`
Notix class to perform all Actions on Notix Api Constructor parameters for this class are `app_id`, `token` which is used for authentication.
# Methods Available
Every method defined inside this class returns [ResponseParser](../../notix/response_parser/) object.
## Checking Authentication 
!!! note "notix.notix_api.Notix.check_auth"
        * `check_auth` Check API auth (sandbox)
            * `parameters` None
            * `description` - Check authorisation without any additional actions as described [here](https://docs.notix.co/api-check-auth.html)


## User identifiers synchronization 
!!! note "notix.notix_api.Notix.remove_add_audience_with_pixel"
        * `remove_add_audience_with_pixel` Synchronised Users
            * `parameters` - `pixel` id **type str**
            * `description` - Perform cookie sync between publisher and Notix as described [here](https://docs.notix.co/user-sync.html)


## Send push messages 
!!! note "notix.notix_api.Notix.send_notification"
        * `send_notification` Send Push Message to users
            * `parameters` 
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
            * `description` - Send notification to a list of subscribers as described [here](https://docs.notix.co/api-send.html)


## Add Audiences
!!! note "notix.notix_api.Notix.add_audience"
        * `add_audience` Add audience
            * `parameters` 
                * `audience` - Audience  Identifier
                * `user` - User Identifier
            * `description` - Add audience label to already subscribed user as described [here](https://docs.notix.co/api-audience.html)

## Delete Audiences
!!! note "notix.notix_api.Notix.delete_audience"
        * `delete_audience` Delete audience
            * `parameters` 
                * `audience` - Audience  Identifier
                * `user` - User Identifier
            * `description` - Delete audience label from your subscriber as described [here](https://docs.notix.co/api-audience.html)


## Audience add or delete using retargeting pixel
!!! note "notix.notix_api.Notix.remove_add_audience_with_pixel"
        * `remove_add_audience_with_pixel` Audience add and delete
            * `parameters` - `pixel` id **type str**
            * `description` - Add or delete user audiences using image pixel as described [here](https://docs.notix.co/retargeting-pixel.html)