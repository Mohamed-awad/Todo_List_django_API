# Signup API Endpoint


### Usage

* This endpoint is used to create new user in our todo list app.


|  API location source |   HTTP Method	| Content Type	|
 |---	               |---	            |---
|  ^api/users/signup/  |      POST      |     JSON      |


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

    |  Field   | Type   | Notes                 |
    |--------|-----------------------|---	       |
    |  status  | number |                       |
    |  message | String |                       |
    |  data | dictionary | contain new user data |


### Samples

1. **Signup request **

    * > request

            {
                "username": "mohamed4",
                "password": "medo@123",
            }

    * > response

            {
                "status": "200",
                "message": "user created successfully",
                "data": {
                  "id": 5,
                  "username": "mohamed4",
                  "password": "medo@123"
               }
            }




2. **Examples of failure cases**

    2.1 username already exists

                {
                    "username": [
                         "A user with that username already exists."
                    ]
                }
