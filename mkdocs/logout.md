# Logout API Endpoint


### Usage

* This endpoint is used to logout the user from our todo list app.


|  API location source | HTTP Method	 | Content Type	|
 |--------------|---	            |---
|  ^api/users/logout/  | GET          |     JSON      |


### Headers
```
{
    "Content-Type": "application/json",
    "Authorization": "Token 125ccc7e48298188747c8d48556eea9f6854b6f0"
}
```

### Response
1. **Response Parameters**

    |  Field   | Type   | Notes                 |
    |--------|-----------------------|---	       |
    |  status  | number |                       |
    |  message | String |                       |
    |  data | dictionary |  |


### Samples

1. **Logout request **

    * > response

            {
                "status": "200",
                "message": "logout successfully",
                "data": {}
            }




2. **Examples of failure cases**

    2.1 Invalid Token

        {
             "detail": "Invalid token."
        }
