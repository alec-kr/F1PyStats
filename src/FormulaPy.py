import drivers_results as d_res
import constructors_results as c_res
import race_results as race_res

import requests
import pandas as pd
from bs4 import BeautifulSoup

def driver_standings(year):
    page = requests.get("https://www.formula1.com/en/results.html/{}/drivers.html".format(year))

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    positions = d_res.get_positions(table)
    names = d_res.get_names(table)
    teams = d_res.get_driver_teams(table)
    nationalities = d_res.get_nationalities(table)
    points = d_res.get_points(table)

    wdc_df = pd.DataFrame(list(zip(positions, names, teams, nationalities, points)), columns=["POS","Driver","Constructor","Nationality","Points"])
    return wdc_df

def constructor_standings(year):
    page = requests.get("https://www.formula1.com/en/results.html/{}/team.html".format(year))

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    positions = d_res.get_positions(table)
    teams = c_res.get_constructors(table)
    points = d_res.get_points(table)

    wcc_df = pd.DataFrame(list(zip(positions, teams, points)), columns=["POS","Constructor","Points"])

    return wcc_df

def race_results(year):
    page = requests.get("https://www.formula1.com/en/results.html/{}/races.html".format(year))

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    grand_prix = race_res.get_grands_prix(table)
    race_date = race_res.get_race_dates(table)
    winner = d_res.get_names(table)
    winning_constructor = race_res.get_winning_constructors(table)
    race_time = race_res.get_race_time(table)
    race_laps = race_res.get_race_laps(table)

    wcc_df = pd.DataFrame(list(zip(grand_prix, race_date, winner, winning_constructor, race_laps, race_time)), columns=["Grand Prix","Date", "Winner", "Team","Laps","Time"])

    return wcc_df

print(race_results(2009))
print(constructor_standings(2007))
print(driver_standings(1999))