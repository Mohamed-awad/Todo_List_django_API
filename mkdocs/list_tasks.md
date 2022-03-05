# List Tasks API Endpoint


### Usage

* This endpoint is used to list all current user tasks.


|  API location source | HTTP Method	 | Content Type	|
 |--------------|---	            |---
|  ^api/tasks/  | GET          |     JSON      |


### Headers
```
{
    "Content-Type": "application/json",
    "Authorization": "Token 125ccc7e48298188747c8d48556eea9f6854b6f0"
}
```

### Response
1. **Response Parameters**

    |  Field   | Type       | Notes                 |
    |------------|--------------|---	       |
    |  status  | number     |                       |
    |  message | String     |                       |
    |  data | dictionary |  |


### Samples

1. **List Tasks request **

    * > response

            {
              "status": "200",
               "message": "success",
               "data": {
                  "count": 3,
                  "next": null,
                  "previous": null,
                  "results": [
                    {
                       "id": 3,
                       "title": "t1",
                       "description": "dddd",
                       "end_user": 2,
                       "status": "P",
                       "due_date": null,
                       "created_at": "2022-03-04T21:49:47.796042Z",
                       "updated_at": "2022-03-04T21:49:47.796131Z"
                    },
                    {
                      "id": 2,
                      "title": "ttttt",
                      "description": "fffff",
                      "end_user": 2,
                      "status": "P",
                      "due_date": "2022-03-01T23:18:38Z",
                      "created_at": "2022-03-03T23:19:30.856492Z",
                      "updated_at": "2022-03-04T21:49:55.506280Z"
                    },
                    {
                      "id": 1,
                      "title": "make admin panel",
                      "description": "cdfvbgbgbbb",
                      "end_user": 2,
                      "status": "F",
                      "due_date": "2022-03-04T23:18:38Z",
                      "created_at": "2022-03-03T23:18:40.425379Z",
                      "updated_at": "2022-03-03T23:25:43.621550Z"
                    }
                  ]
               }
            }
