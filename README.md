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
Send post request to  `http://where.seeleit.com/`. In post method, your data in post request must contain the following two values: `{'lng': 100, 'lat':100}`  



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

## Test
I provide a locust file (locustfile.py) to test the service. See [LOCUST](http://locust.io/) here. Run `locust --host=http://where.seeleit.com/` under `tests/` and you can access a web interface at http://127.0.0.1:8089/


## Attention
1. The default area range is x, y from -500 to 500 respectively.
2. We calculate the distance based on the line distance of the grid instead of Euclidean Distance. For exmaple, the distance between [1,1] and [0,0] is 2, not sqrt(2).
3. Locations are static and stored in several files as is shown below.
	```
	100,100
	-60,80
	70,-250
	...
	```
	In order to optimize the efficiency, I try to partition the whole map to small areas of same size. Each area with a specific file. It is critical that putting locations within appropriate file for other services which will modify these static files.
	


### Deployed Environment
Server: Aliyun Ubuntu14.04, Core: 2, RAM: 4G, Python: 2.7.6
