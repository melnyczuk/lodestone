# Lodestone
geolocation &rarr; orientation 
---
![](https://upload.wikimedia.org/wikipedia/commons/2/20/Lodestone_attracting_nails.png)

Lodestone is a service that takes a geolocation and returns an angle of orientation around that point.

All endpoints work in the following way:
- `POST` to `/endpoint` accepts a `{ lat: float, lng: float }` json body and returns a `task_id`
- `GET` to `/endpoint/<task_id>` returns the data from the task (if complete) or information about the status of the task

All response objects follow the same shape:
- `result` the successful result of the process
- `error` and unsuccessful process (including pending processes)

## Routes
| endpoint | description |
|---|---|
| `/ratings` | uses google places ratings |

## Dev
To run in dev on port 5000:
- `$ docker-compose -f ./docker-compose.dev.yml up`
- `$ pipenv run dev` or `$ pipenv run dev-http`

The server needs a dummy cert and key to be run using HTTPS.

To generate these:
```
openssl req -x509 -out localhost.crt -keyout localhost.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")
```
