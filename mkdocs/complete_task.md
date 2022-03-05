# Complete Task API Endpoint


### Usage

* This endpoint is used to mark task as finished.


| API location source | HTTP Method	 | Content Type	|
 |---                |--------------|---	 
| ^api/tasks/<task_id>/complete/      | GET          |     JSON      |


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

1. **Complete request **

    * > response

            {
                "status": "200",
                "message": "task marked as completed successfully",
                "data": {}
            }




2. **Examples of failure cases**

    2.1 Task not found

        {
             "status": 404,
             "message": "task not found",
             "data": {}
        }
