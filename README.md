# lode-stone
geolocation &rarr; orientation
![](https://upload.wikimedia.org/wikipedia/commons/2/20/Lodestone_attracting_nails.png)

### Lodestone is a service that takes a geolocation and returns an angle of orientation around that point.

All endpoints accept a `GET` request with a query string containing `lng` and `lat` float values. 

`?lng=0.0&lat=0.0`

## Routes
| | |
|---|---|
| `/ratings` | uses google places ratings |
