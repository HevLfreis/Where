# Where
Where is a web service to simulate finding nearest cars of taxi-booking-apps  
Location: http://where.seeleit.com/  

***

## What is this ?
Where is a web service to simulate finding nearest cars of taxi-booking-apps. Considering that we have an NxN grid, some points of the grid have already placed taxis. You are on one certain point on the grid and we'd like to find which taxi is the nearest to your location.

## How to use
I provide two ways to access the service:  
1. GET  
Example:  `http://where.seeleit.com/?lng=100&lat=100`  
2. POST  
In post method, your data in post request must contain the following two values: `{'lng': 100, 'lat':100}`  



## Return value
The service will return the top2 nearest positions correponding to your request in json format:
for example
`{
  "locations": [
    [
      -54, 
      3
    ], 
    [
      -46, 
      32
    ]
  ]
}`  
The first pair of coordinates is the nearest one and the other is the 2nd nearest one.   

If your parameter is error or out of range, the service will return null:
`{
  "locations": [
    null, 
    null
  ]
}`


## Attention
1. The default area range is x, y from -500 to 500 respectively.


### Deployed Environment
Server: Aliyun Ubuntu14.04, Core: 2, RAM: 4G, Python: 2.7.6
