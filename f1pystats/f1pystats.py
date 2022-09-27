'''This module is responsible for handling the user-level function calls'''

import requests
import pandas as pd

from .driver_results import DriverResults

from .constructor_results import ConstructorResults

from .race_winners import RaceWinners

from .race_schedule import RaceSchedule

from .lap_times import LapTimes


def driver_standings(year: int):
    '''Returns the driver standings for a specified year'''
    link = f"https://ergast.com/api/f1/{year}/driverStandings.json"

    page = requests.get(link, timeout=15)
    json_data = page.json()
    standings_json = json_data["MRData"]["StandingsTable"][
        "StandingsLists"][0][
        "DriverStandings"
    ]

    d_res = DriverResults(standings_json)

    positions = d_res.get_driver_positions()
    names = d_res.get_driver_names()
    teams = d_res.get_driver_teams()
    nationalities = d_res.get_driver_nationality()
    points = d_res.get_driver_points()
    wins = d_res.get_driver_wins()

    wdc_df = pd.DataFrame(
        list(zip(positions, names, nationalities, teams, points, wins)),
        columns=["POS", "Driver", "Nationality",
                 "Constructor", "Points", "Wins"],
    )
    return wdc_df


def constructor_standings(year: int):
    '''Returns the constructor standings for a specified year'''
    link = f"https://ergast.com/api/f1/{year}/constructorStandings.json"
    page = requests.get(link, timeout=15)

    json_data = page.json()
    standings_json = json_data["MRData"]["StandingsTable"][
        "StandingsLists"][0][
        "ConstructorStandings"
    ]

    c_res = ConstructorResults(standings_json)

    positions = c_res.get_constructor_positions()
    teams = c_res.get_constructor_names()
    nationality = c_res.get_constructor_nationality()
    points = c_res.get_constructor_points()
    wins = c_res.get_constructor_wins()

    wcc_df = pd.DataFrame(
        list(zip(positions, teams, nationality, points, wins)),
        columns=["POS", "Constructor", "Nationality", "Points", "Wins"],
    )

    return wcc_df


def race_winners(year: int):
    '''Returns the race winners in a specified year'''
    link = f"https://ergast.com/api/f1/{year}/results/1.json"
    page = requests.get(link, timeout=15)

    json_data = page.json()
    results_json = json_data["MRData"]["RaceTable"]["Races"]

    r_winners = RaceWinners(results_json)

    grands_prix = r_winners.get_grands_prix()
    race_dates = r_winners.get_race_dates()
    winners = r_winners.get_race_winners()
    winning_constructors = r_winners.get_winning_constructors()
    race_laps = r_winners.get_race_laps()
    race_times = r_winners.get_race_times()
    start_positions = r_winners.get_winner_start_positions()

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

    page = requests.get(link, timeout=15)

    json_data = page.json()
    schedule_json = json_data["MRData"]["RaceTable"]["Races"]

    r_sched = RaceSchedule(schedule_json)

    race_round = r_sched.get_race_round()
    race_name = r_sched.get_race_names()
    race_circuits = r_sched.get_race_circuits()
    race_schedule_date = r_sched.get_race_schedule_dates()
    race_schedule_time = r_sched.get_race_schedule_times()
    race_locality = r_sched.get_race_locality()
    race_country = r_sched.get_race_countries()

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


def lap_times(year: int, race_round: int, lap_number: int):
    '''Returns the lap times for a specified year, race round and lap number'''
    link = f"https://ergast.com/api/f1/{year}/{race_round}/laps/{lap_number}.json"

    page = requests.get(link, timeout=15)

    json_data = page.json()
    schedule_json = json_data["MRData"]["RaceTable"]["Races"][0]["Laps"][0]["Timings"]

    l_times = LapTimes(schedule_json)

    driver_names = l_times.get_driver_names()
    driver_positions = l_times.get_driver_positions()
    driver_timings = l_times.get_lap_time()

    wcc_df = pd.DataFrame(
        list(
            zip(
            driver_positions,
            driver_names,
            driver_timings,
            )
        ),
        columns=["POS", "Driver", "Lap Time",
        ],
    )

    return wcc_df
