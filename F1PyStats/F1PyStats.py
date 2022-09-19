from .drivers_results import get_driver_teams, get_names, get_nationalities, get_points, get_positions
from .constructors_results import get_constructors
from .race_results import get_grands_prix, get_race_dates, get_race_laps, get_race_time, get_winning_constructors

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Returns the driver standings for a specific year
def driver_standings(year:int):
    page = requests.get("https://www.formula1.com/en/results.html/{}/drivers.html".format(year))

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    positions = get_positions(table)
    names = get_names(table)
    teams = get_driver_teams(table)
    nationalities = get_nationalities(table)
    points = get_points(table)

    wdc_df = pd.DataFrame(list(zip(positions, names, teams, nationalities, points)), columns=["POS","Driver","Constructor","Nationality","Points"])
    return wdc_df

# Returns the constructor standings for a specific year
def constructor_standings(year:int):
    page = requests.get("https://www.formula1.com/en/results.html/{}/team.html".format(year))

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    positions = get_positions(table)
    teams = get_constructors(table)
    points = get_points(table)

    wcc_df = pd.DataFrame(list(zip(positions, teams, points)), columns=["POS","Constructor","Points"])

    return wcc_df

# Returns all race results for a specific year
def race_results(year:int):
    page = requests.get("https://www.formula1.com/en/results.html/{}/races.html".format(year))

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    grand_prix = get_grands_prix(table)
    race_date = get_race_dates(table)
    winner = get_names(table)
    winning_constructor = get_winning_constructors(table)
    race_time = get_race_time(table)
    race_laps = get_race_laps(table)

    wcc_df = pd.DataFrame(list(zip(grand_prix, race_date, winner, winning_constructor, race_laps, race_time)), columns=["Grand Prix","Date", "Winner", "Team","Laps","Time"])

    return wcc_df