'''This module is responsible for handling the user-level function calls'''

import requests
import pandas as pd

from .driver_results import (
    get_driver_positions,
    get_driver_names,
    get_driver_points,
    get_driver_teams,
    get_driver_wins,
    get_driver_nationality,
)

from .constructor_results import (
    get_constructor_names,
    get_constructor_nationality,
    get_constructor_points,
    get_constructor_positions,
    get_constructor_wins,
)

from .race_winners import (
    get_grands_prix,
    get_race_dates,
    get_race_winners,
    get_winning_constructors,
    get_race_laps,
    get_winner_start_positions,
    get_race_times,
)

from .race_schedule import (
    get_race_round,
    get_race_names,
    get_race_circuits,
    get_race_schedule_dates,
    get_race_schedule_times,
    get_race_locality,
    get_race_countries,
)


def driver_standings(year: int):
    '''Returns the driver standings for a specified year'''
    link = f"https://ergast.com/api/f1/{year}/driverStandings.json"

    page = requests.get(link)
    json_data = page.json()
    standings = json_data["MRData"]["StandingsTable"]["StandingsLists"][0][
        "DriverStandings"
    ]

    positions = get_driver_positions(standings)
    names = get_driver_names(standings)
    teams = get_driver_teams(standings)
    nationalities = get_driver_nationality(standings)
    points = get_driver_points(standings)
    wins = get_driver_wins(standings)

    wdc_df = pd.DataFrame(
        list(zip(positions, names, nationalities, teams, points, wins)),
        columns=["POS", "Driver", "Nationality",
                 "Constructor", "Points", "Wins"],
    )
    return wdc_df


def constructor_standings(year: int):
    '''Returns the constructor standings for a specified year'''
    link = f"https://ergast.com/api/f1/{year}/constructorStandings.json"
    page = requests.get(link)

    json_data = page.json()
    standings = json_data["MRData"]["StandingsTable"]["StandingsLists"][0][
        "ConstructorStandings"
    ]

    positions = get_constructor_positions(standings)
    teams = get_constructor_names(standings)
    nationality = get_constructor_nationality(standings)
    points = get_constructor_points(standings)
    wins = get_constructor_wins(standings)

    wcc_df = pd.DataFrame(
        list(zip(positions, teams, nationality, points, wins)),
        columns=["POS", "Constructor", "Nationality", "Points", "Wins"],
    )

    return wcc_df


def race_winners(year: int):
    '''Returns the race winners in a specified year'''
    link = f"https://ergast.com/api/f1/{year}/results/1.json"
    page = requests.get(link)

    json_data = page.json()
    results = json_data["MRData"]["RaceTable"]["Races"]

    grands_prix = get_grands_prix(results)
    race_dates = get_race_dates(results)
    winners = get_race_winners(results)
    winning_constructors = get_winning_constructors(results)
    race_laps = get_race_laps(results)
    race_times = get_race_times(results)
    start_positions = get_winner_start_positions(results)

    wcc_df = pd.DataFrame(
        list(
            zip(
                grands_prix,
                race_dates,
                winners,
                winning_constructors,
                race_laps,
                race_times,
                start_positions,
            )
        ),
        columns=["Grand Prix", "Date", "Winner",
                 "Constructor", "Laps", "Time", "Grid"],
    )

    return wcc_df


def race_table(year: int):
    '''Returns the race schedule for a specified year'''
    link = f"https://ergast.com/api/f1/{year}.json"

    page = requests.get(link)

    json_data = page.json()
    r_schedule = json_data["MRData"]["RaceTable"]["Races"]

    race_round = get_race_round(r_schedule)
    race_name = get_race_names(r_schedule)
    race_circuits = get_race_circuits(r_schedule)
    race_schedule_date = get_race_schedule_dates(r_schedule)
    race_schedule_time = get_race_schedule_times(r_schedule)
    race_locality = get_race_locality(r_schedule)
    race_country = get_race_countries(r_schedule)

    wcc_df = pd.DataFrame(
        list(
            zip(
                race_round,
                race_name,
                race_circuits,
                race_schedule_date,
                race_schedule_time,
                race_locality,
                race_country,
            )
        ),
        columns=[
            "Round",
            "Race Name",
            "Circuit",
            "Date",
            "Time",
            "Locality",
            "Country",
        ],
    )

    return wcc_df
