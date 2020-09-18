# Lodestone
geolocation &rarr; orientation 
---
![](https://upload.wikimedia.org/wikipedia/commons/2/20/Lodestone_attracting_nails.png)

Lodestone is a service that takes a geolocation and returns an angle of orientation around that point.

All endpoints work in the following way:
- `POST` to `/endpoint` accepts a `{ lat: float, lng: float }` json body and returns a `task_id`
- `GET` to `/endpoint/<task_id>` returns the data from the task (if complete) or information about the status of the task

## Routes
| endpoint | description |
|---|---|
| `/ratings` | uses google places ratings |
