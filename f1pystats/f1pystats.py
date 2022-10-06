"""This module is responsible for handling the user-level function calls"""

import requests
import pandas as pd

from .pit_stops import PitStops

from .driver_results import DriverResults

from .constructor_results import ConstructorResults

from .race_winners import RaceWinners

from .race_schedule import RaceSchedule

from .lap_times import LapTimes
from .finishing_status import FinishingStatus

from .driver_info import DriverInfo

from .constructor_info import ConstructorInfo


def get_drivers(year: int, round_num: int = None):
    """Returns a list of drivers for a specified year"""
    if round_num is None:
        json_data = _get_json_content_from_url(f"https://ergast.com/api/f1/{year}/drivers.json")
    else:
        json_data = _get_json_content_from_url(
            f"https://ergast.com/api/f1/{year}/{round_num}/drivers.json"
        )

    dr_info = DriverInfo(json_data["MRData"]["DriverTable"]["Drivers"])

    dr_name = dr_info.get_drivers_names()
    dr_dob = dr_info.get_drivers_dob()
    dr_nationality = dr_info.get_drivers_nationality()
    dr_perm_number = dr_info.get_drivers_number()

    return pd.DataFrame(
        zip(dr_name, dr_perm_number, dr_nationality, dr_dob),
        columns=["Drivers", "Permanent Number", "Nationality", "Date of Birth"],
    )


def driver_standings(year: int):
    """Returns the driver standings for a specified year"""
    json_data = _get_json_content_from_url(f"https://ergast.com/api/f1/{year}/driverStandings.json")
    standings_json = json_data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    d_res = DriverResults(standings_json)
    positions = d_res.get_driver_positions()
    names = d_res.get_driver_names()
    teams = d_res.get_driver_teams()
    nationalities = d_res.get_driver_nationality()
    points = d_res.get_driver_points()
    wins = d_res.get_driver_wins()

    return pd.DataFrame(
        zip(positions, names, nationalities, teams, points, wins),
        columns=["POS", "Driver", "Nationality", "Constructor", "Points", "Wins"],
    )


def constructor_standings(year: int):
    """Returns the constructor standings for a specified year"""
    json_data = _get_json_content_from_url(
        f"https://ergast.com/api/f1/{year}/constructorStandings.json"
    )
    standings_json = json_data["MRData"]["StandingsTable"]["StandingsLists"][0][
        "ConstructorStandings"
    ]
    c_res = ConstructorResults(standings_json)
    positions = c_res.get_constructor_positions()
    teams = c_res.get_constructor_names()
    nationality = c_res.get_constructor_nationality()
    points = c_res.get_constructor_points()
    wins = c_res.get_constructor_wins()

    return pd.DataFrame(
        zip(positions, teams, nationality, points, wins),
        columns=["POS", "Constructor", "Nationality", "Points", "Wins"],
    )


def race_winners(year: int):
    """Returns the race winners in a specified year"""
    json_data = _get_json_content_from_url(f"https://ergast.com/api/f1/{year}/results/1.json")
    results_json = json_data["MRData"]["RaceTable"]["Races"]
    r_winners = RaceWinners(results_json)
    grands_prix = r_winners.get_grands_prix()
    race_dates = r_winners.get_race_dates()
    winners = r_winners.get_race_winners()
    winning_constructors = r_winners.get_winning_constructors()
    race_laps = r_winners.get_race_laps()
    race_times = r_winners.get_race_times()
    start_positions = r_winners.get_winner_start_positions()

    return pd.DataFrame(
        zip(
            grands_prix,
            race_dates,
            winners,
            winning_constructors,
            race_laps,
            race_times,
            start_positions,
        ),
        columns=["Grand Prix", "Date", "Winner", "Constructor", "Laps", "Race Time", "Grid"],
    )


def race_table(year: int):
    """Returns the race schedule for a specified year"""
    json_data = _get_json_content_from_url(f"https://ergast.com/api/f1/{year}.json")
    schedule_json = json_data["MRData"]["RaceTable"]["Races"]
    r_sched = RaceSchedule(schedule_json)
    race_round = r_sched.get_race_round()
    race_name = r_sched.get_race_names()
    race_circuits = r_sched.get_race_circuits()
    race_schedule_date = r_sched.get_race_schedule_dates()
    race_schedule_time = r_sched.get_race_schedule_times()
    race_locality = r_sched.get_race_locality()
    race_country = r_sched.get_race_countries()

    return pd.DataFrame(
        zip(
            race_round,
            race_name,
            race_circuits,
            race_schedule_date,
            race_schedule_time,
            race_locality,
            race_country,
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


def lap_times(year: int, race_round: int, lap_number: int):
    """Returns the lap times for a specified year, race round and lap number"""
    json_data = _get_json_content_from_url(
        f"https://ergast.com/api/f1/{year}/{race_round}/laps/{lap_number}.json"
    )
    schedule_json = json_data["MRData"]["RaceTable"]["Races"][0]["Laps"][0]["Timings"]
    l_times = LapTimes(schedule_json)
    driver_names = l_times.get_driver_names()
    driver_positions = l_times.get_driver_positions()
    driver_timings = l_times.get_lap_time()

    return pd.DataFrame(
        zip(
            driver_positions,
            driver_names,
            driver_timings,
        ),
        columns=[
            "POS",
            "Driver",
            "Lap Time",
        ],
    )


def pit_stops(year: int, race_round: int, stop_number: int = 0):
    """Returns the pit stops for a specific race in a season"""
    if int == 0:
        json_data = _get_json_content_from_url(
            f"https://ergast.com/api/f1/{year}/{race_round}/pitstops.json"
        )
    else:
        json_data = _get_json_content_from_url(
            f"https://ergast.com/api/f1/{year}/{race_round}/pitstops/{stop_number}.json"
        )
    stops_json = json_data["MRData"]["RaceTable"]["Races"][0]["PitStops"]
    p_stops = PitStops(stops_json)
    driver_names = p_stops.get_driver_names()
    stop_number = p_stops.get_stop_numbers()
    lap_number = p_stops.get_lap_numbers()
    race_time = p_stops.get_times()
    stop_duration = p_stops.get_durations()

    return pd.DataFrame(
        zip(driver_names, stop_number, lap_number, race_time, stop_duration),
        columns=["Driver", "Stop", "Lap", "Time", "Duration"],
    )


def finishing_status(year: int, race_round: int = 0):
    """Returns the finishing status for a year with a optional parameter of round"""
    if race_round == 0:
        json_data = _get_json_content_from_url(f"https://ergast.com/api/f1/{year}/status.json")
    else:
        json_data = _get_json_content_from_url(
            f"https://ergast.com/api/f1/{year}/{race_round}/status.json"
        )
    f_status = FinishingStatus(json_data["MRData"]["StatusTable"]["Status"])
    status_id = f_status.get_status_id()
    status_info = f_status.get_status()
    status_count = f_status.get_status_count()

    return pd.DataFrame(
        zip(status_id, status_info, status_count), columns=["StatusId", "Status", "Count"]
    )

def get_constructors(year: int = None):
    """Returns a list of constructors for a specified year"""

    if year is None:
        url = "http://ergast.com/api/f1/constructors.json"
    else:
        url = f"http://ergast.com/api/f1/{year}/constructors.json"

    json_data = _get_json_content_from_url(url)

    constructors_info = ConstructorInfo(json_data["MRData"]["ConstructorTable"]["Constructors"])

    constructors_names = constructors_info.get_constructors_names()
    constructors_nationalities = constructors_info.get_constructors_nationality()

    return pd.DataFrame(
        zip(constructors_names, constructors_nationalities),
        columns=["Constructor", "Nationality"],
    )

def _get_json_content_from_url(url, *args, timeout: int = 15, **kwargs):
    """Returns JSON content from requestsm URL"""
    return requests.get(url, *args, timeout=timeout, **kwargs).json()
