# RoutesOptimizer

A Python Script that find alternative routes based on certain features
Specify which restaurant you want the most on the path. 
The algorithm will pick the path that has the most specified shop.
Very accurate results but is the algorithm is a little slow. O(N^2)

If the same shop is within 10 km of each other it will not inlude it in the shop frequency

## Example
Finds the Route with most Taco Bells without addition of too much time

Search Term is 'Taco Bell'

Origin: New York 

Destination: Kansas City
```
NEW----------------------------------ROUTE
Route Distance: 1189.5953017272727 Miles
Route Duration: 18.124444444444446 Hours
Total Shops Regions: 33
Total Shops: 75
NEW----------------------------------ROUTE
Route Distance: 1216.0514238257574 Miles
Route Duration: 18.345 Hours
Total Shops Regions: 36
Total Shops: 81
NEW----------------------------------ROUTE
Route Distance: 1224.6884836742424 Miles
Route Duration: 18.725 Hours
Total Shops Regions: 35
Total Shops: 75

```

## Tools
Yelp Search API

Google Map API

Zipcode Searcher

## Details
Finds the correct Route without add too much time to the route beacuase the lat and long of direction change
You can change after how many miles does the algorithm look. The smaller the mile value, the faster the program

## Future
Going to add a option that finds the path with best weather Ex: path without storms, rain, etc.

