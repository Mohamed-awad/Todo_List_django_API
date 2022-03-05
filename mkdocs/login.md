# Login API Endpoint


### Usage

* This endpoint is used to generate token for current user.


| API location source |   HTTP Method	| Content Type	|
|---	               |---	            |---
| ^api/users/login/   |      POST      |     JSON      |


### Headers
```
{
    "Content-Type": "application/json",
}
```


### Request
1. **Request Parameters**

    |  Field           |   M/O/C  |    Type           | Notes |
    |-------	       |------    |-------|-------   |
    | username         |   M      |   String          |       |
    | password         |   M      |   String           |       |
    


### Response
1. **Response Parameters**

    |  Field   | Type   | Notes                         |
    |--------|-------------------------------|---	       |
    |  status  | number |                               |
    |  message | String |                               |
    |  data | dictionary | contain current user data + token |


### Samples

1. **Login request **

    * > request

            {
                "username": "mohamed4",
                "password": "medo@123",
            }

    * > response

            {
                "status": "200",
                "message": "token generated successfully",
                "data": {
                  "token": "07914a38308560fcf0fdbd49d68e6134be3030d0",
                  "user_id": 2,
                  "username": "mohamed"
               }
            }




2. **Examples of failure cases**

    2.1 Invalid credentials

                {
                    "non_field_errors": [
                       "Unable to log in with provided credentials."
                    ]
                }
