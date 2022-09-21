# F1PyStats
F1PyStats is an open-source Python3 package that provides Formula 1 data to developers.

This package scrapes data from the official [Formula 1 website](https://formula1.com/), and returns data in a pandas DataFrame format.

# Installation
```
// Clone the repo
$ git clone https://github.com/alec-kr/F1PyStats.git

// Install dependencies
$ pip install bs4 pandas requests

// Install the package
$ pip install path/to/F1PyStats/
```

# Usage
```
# Import the package
import F1PyStats as fp
```

The package currently contains four functions
| Function                    	| Description                                                         	| Returned Datatype 	|
|-----------------------------	|---------------------------------------------------------------------	|-------------------	|
| fp.driver_standings(year)      	| Returns the driver standings for a particular year                  	| Pandas DataFrame  	|
| fp.constructor_standings(year) 	| Returns the constructor standings for a specified year              	| Pandas DataFrame  	|
| fp.race_results(year)          	| Returns the race results for a specified year                       	| Pandas DataFrame  	|
| fp.fastest_lap(year)           	| Returns the fastest lap times for each race, during a specific year 	| Pandas DataFrame  	|

# Contributions
- Have a feature you would like to add? Feel free to create a PR :smile:.
- Spot an issue or bug? Please let me know by creating an issue.
