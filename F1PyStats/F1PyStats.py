from .drivers_results import (get_names,
                              get_nationalities,
                              get_points,
                              get_positions)

from .constructors_results import get_constructors
from .race_results import (get_grands_prix,
                           get_race_dates,
                           get_race_laps,
                           get_race_time)

import requests
import pandas as pd
from bs4 import BeautifulSoup


def driver_standings(year: int):
    link = "https://www.formula1.com/en/results.html/{}/drivers.html".\
            format(year)

    page = requests.get(link)

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    positions = get_positions(table)
    names = get_names(table)
    teams = get_constructors(table, "drivers_results")
    nationalities = get_nationalities(table)
    points = get_points(table)

    wdc_df = pd.DataFrame(list(
                            zip(positions,
                                names,
                                teams,
                                nationalities,
                                points)),
                          columns=["POS", "Driver",
                                   "Constructor", "Nationality",
                                   "Points"])
    return wdc_df


def constructor_standings(year: int):
    link = "https://www.formula1.com/en/results.html/{}/team.html".\
            format(year)
    page = requests.get(link)

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    positions = get_positions(table)
    teams = get_constructors(table, "team_standings")
    points = get_points(table)

    wcc_df = pd.DataFrame(list(
                        zip(positions, teams, points)),
                        columns=["POS", "Constructor", "Points"])

    return wcc_df


def race_results(year: int):
    link = "https://www.formula1.com/en/results.html/{}/races.html".\
            format(year)
    page = requests.get(link)

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    grand_prix = get_grands_prix(table, "race_results")
    race_date = get_race_dates(table)
    winner = get_names(table)
    winning_constructor = get_constructors(table, "race_results")
    race_time = get_race_time(table, "race_results")
    race_laps = get_race_laps(table)

    wcc_df = pd.DataFrame(list(
                        zip(grand_prix, race_date, winner,
                            winning_constructor, race_laps,
                            race_time)),
                          columns=["Grand Prix", "Date",
                                   "Winner", "Team",
                                   "Laps", "Time"])

    return wcc_df


def fastest_lap(year: int):
    link = "https://www.formula1.com/en/results.html/{}/fastest-laps.html".\
            format(year)
    page = requests.get(link)

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    grands_prix = get_grands_prix(table, "fastest_lap")
    drivers = get_names(table)
    teams = get_constructors(table, "fastest_lap")
    race_time = get_race_time(table, "fastest_lap")

    wcc_df = pd.DataFrame(list(
                        zip(grands_prix, drivers, teams, race_time)),
                        columns=["Grand Prix", "Driver", "Team", "Time"])

    return wcc_df