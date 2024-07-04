
# URL Shorter API (Django Rest Framework)

This is a simple API of a url shorter


```python
pip install -r requirements.txt
```
## API Reference

#### Get all urls

```http
  GET /api/get_all_urls
```

```json
{
    "urls": [
        {
            "id": 1,
            "code": "b337d5d5",
            "url": "https://aminehalal.vercel.app/",
            "num_visits": "1",
            "createdAT": "2024-07-03T17:22:45.758796Z"
        },
        {
            "id": 2,
            "code": "35c6a2c7",
            "url": "https://www.facebook.com/aminenohalal/",
            "num_visits": "0",
            "createdAT": "2024-07-03T17:40:11.637194Z"
        },
        {
            "id": 3,
            "code": "49d9ac63",
            "url": "https://www.facebook.com/aminenohalal/",
            "num_visits": "0",
            "createdAT": "2024-07-03T17:40:41.245379Z"
        },
        {
            "id": 4,
            "code": "85e7dff4",
            "url": "https://www.facebook.com/aminenohalal/",
            "num_visits": "0",
            "createdAT": "2024-07-03T17:41:00.984066Z"
        },
    ]
}
```

#### Get url

```http
  GET /api/get_url/${code}
```

```json
{
    "url": {
        "id": 4,
        "code": "85e7dff4",
        "url": "https://www.facebook.com/aminenohalal/",
        "num_visits": "0",
        "createdAT": "2024-07-03T17:41:00.984066Z"
    }
}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `code`      | `string` | **Required**. Code of url to fetch |

#### Post a url

```http
  POST /api/url
```

```json
{
    "url" : "Your Url"
}
```
###### Result

```json
{
    "id": 7,
    "code": "265603eb",
    "url": "Your url",
    "num_visits": "0",
    "createdAT": "2024-07-04T13:38:36.553714Z"
}
```

#### Visit a website

```http
  GET /${code}
```

Will be redirected to the website who had this code

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `code`      | `string` | **Required**. Code of url to fetch |






## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://aminehalal.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aminehalal/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/aminenohalal)

