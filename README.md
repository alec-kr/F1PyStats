# F1PyStats
<img src="https://raw.githubusercontent.com/alec-kr/F1PyStats/main/assets/F1PYStatsSimplified.png" align="right" alt="icon" width="303">

[![GitHub Repo stars](https://img.shields.io/github/stars/alec-kr/F1PyStats?style=social)](https://github.com/alec-kr/F1PyStats)
[![GitHub forks](https://img.shields.io/github/forks/alec-kr/F1PyStats?style=social)](https://github.com/alec-kr/F1PyStats/network/members)

[![GitHub Hacktoberfest combined status](https://img.shields.io/github/hacktoberfest/2022/alec-kr/F1PyStats)](https://github.com/alec-kr/F1PyStats)
[![codecov](https://codecov.io/gh/alec-kr/F1PyStats/branch/main/graph/badge.svg?token=75FEMX2BHQ)](https://codecov.io/gh/alec-kr/F1PyStats)
[![GitHub](https://img.shields.io/github/license/alec-kr/F1PyStats?color=blue)](https://github.com/alec-kr/F1PyStats/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/alec-kr/F1PyStats)](https://github.com/alec-kr/F1PyStats/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/alec-kr/F1PyStats)](https://github.com/alec-kr/F1PyStats/pulls)
[![GitHub contributors](https://img.shields.io/github/contributors/alec-kr/F1PyStats)](https://github.com/alec-kr/F1PyStats/graphs/contributors)

F1PyStats is an open-source Python3 package that provides Formula 1 data/statistics to developers. This package obtains Formula 1 data via the [Ergast Developer API](http://ergast.com/mrd/), and returns results in a pandas DataFrame format.


# Prerequisites
## Python3
Before installing the package, you should ensure your Python version is at least [v3.8](https://www.python.org/downloads/release/python-380/). If your version does not meet the requirements, please [download](https://www.python.org/downloads/) a newer version to ensure the package works as expected.

## Poetry
The package uses [Poetry](https://python-poetry.org/) as the primary dependency management tool. To install this tool, kindly follow their [official installation instructions](https://python-poetry.org/docs/).

# Installation
```
// Clone the repo
$ git clone https://github.com/alec-kr/F1PyStats.git

// Install dependecies using poetry
$ cd ../F1PyStats
$ poetry install --only main

// Build the package if you would to use it in other projects (https://python-poetry.org/docs/cli/#build)
poetry build

// Install built package (https://python-poetry.org/docs/cli/#add)
poetry add ../F1Pystats/dist/f1pystats-0.1.0.whl
```

# Usage
```
# Import the package
import F1PyStats as fp
```

The package currently contains twelve functions
| Function                    	| Description                                                         	| Returned Datatype 	|
|-----------------------------	|---------------------------------------------------------------------	|-------------------	|
| fp.driver_standings(year)      	| Returns the driver standings for a particular year                  	| Pandas DataFrame  	|
| fp.constructor_standings(year) 	| Returns the constructor standings for a specified year              	| Pandas DataFrame  	|
| fp.race_winners(year)          	| Returns the race winners for a specified year                       	| Pandas DataFrame  	|
| fp.race_table(year)           	| Returns the race schedule for a specific year 	                      | Pandas DataFrame  	|
| fp.lap_times(year, race_round, lap_number)           	| Returns the lap times for a specific lap in a particular race 	                      | Pandas DataFrame  	|
| fp.pit_stops(year, round, stop_number)           	| Returns the pit stop info for a specific race/pit stop 	                      | Pandas DataFrame  	|
| fp.finishing_status(year,race_round)  | Returns the finishing status of races in a year (or a particular race if specified)     | Pandas DataFrame  |
|fp.get_drivers(year, race_round) | Returns information on drivers in a given year (or a particular race if specified) | Pandas DataFrame |
|fp.get_constructors(year) | Returns information on constructors in a given year | Pandas DataFrame |
|fp.sprint_results(year,race_round) | Returns the sprint qualifying results for a specific race | Pandas DataFrame|
|fp.qualifying_results(year, race_round) | Returns the qualifying results of a particular race | Pandas DataFrame |
|fp.get_circuits(year) | Returns the circuit details of a specific race for a specific year| Pandas DataFrame |



# Contributions
NOTE: Please ensure you follow our [contributing guidelines](https://github.com/alec-kr/F1PyStats/blob/main/CONTRIBUTING.md) when contributing in any way to this repository.
## Feature Requests
Perhaps you have a great idea for a feature, but you're not sure how to implement it. 

No worries! You can [create a feature request](https://github.com/alec-kr/F1PyStats/issues/new/choose), and someone will get in touch with you :grin:

## Creating PRs
Know how to code and you'd like to add a feature? Feel free to [create a PR](https://github.com/alec-kr/F1PyStats/compare) :rocket:

## Bug Reports
Spot an issue or bug? Please let us know by [creating a bug report](https://github.com/alec-kr/F1PyStats/issues/new/choose) :bug:

## OUR VALUABLE CONTRIBUTORS✨
<p align="center">
  

<a href="https://github.com/alec-kr/F1PyStats/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alec-kr/F1PyStats" />
</a>
</p>
<h3 align=center>Happy Coding 👨‍💻 </h3>
