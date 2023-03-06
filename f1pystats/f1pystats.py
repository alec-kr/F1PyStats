"""This module is responsible for handling the user-level function calls"""

from typing import Optional
import pandas as pd
import requests
from requests.adapters import HTTPAdapter

from .constructor_info import ConstructorInfo
from .constructor_results import ConstructorResults
from .driver_info import DriverInfo
from .driver_results import DriverResults
from .finishing_status import FinishingStatus
from .lap_times import LapTimes
from .pit_stops import PitStops
from .qualifying_results import QualifyingResults
from .race_circuits import RaceCircuits
from .race_schedule import RaceSchedule
from .race_winners import RaceWinners
from .sprint_results import SprintResults


def _get_json_content_from_url(url, *args, timeout: int = 15, **kwargs):
    """Returns JSON content from requestsm URL"""
    session = requests.Session()
    session.mount('https://ergast.com', HTTPAdapter(max_retries=2))
    return session.get(url, *args, timeout=timeout, **kwargs).json()


def get_sec(time_str):
    """Returns seconds from time string"""
    sec = 0
    num = 0
    dplace = 0
    for char in time_str:
        if dplace == 0:
            if '0' <= char <= '9':
                num *= 10
                num += ord(char) - ord('0')
            elif char == ':':
                sec += num
                sec *= 60
                num = 0
            elif char == '.':
                sec += num
                num = 0
                dplace = -1
        else:
            if '0' <= char <= '9':
                num *= 10
                num += ord(char) - ord('0')
                dplace -= 1

    if dplace == 0:
        sec += num
    else:
        sec += num * pow(10, dplace + 1)

    return sec


# Requesting the season list and get the last one to initialize CURR_YEAR
CURR_YEAR = int(
    _get_json_content_from_url(
        "http://ergast.com/api/f1/seasons.json?limit=200"
    )["MRData"]["SeasonTable"]["Seasons"][-1]["season"]
)


def get_drivers(year: int, round_num: Optional[int] = None):
    """Returns a list of drivers for a specified year"""
    if year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )
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
    if year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )

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
    if year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )

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
    if year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )

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
    if year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )

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
    if year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )

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


def pit_stops(year: int, race_round: int, stop_number: int = 0, fastest: bool = False):
    """Returns the pit stops for a specific race in a season"""
    if year < 2012 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 2012 and {CURR_YEAR} are considered as valid value for year"
        )

    if stop_number == 0:
        json_data = _get_json_content_from_url(
            f"https://ergast.com/api/f1/{year}/{race_round}/pitstops.json"
        )
    else:
        json_data = _get_json_content_from_url(
            f"https://ergast.com/api/f1/{year}/{race_round}/pitstops/{stop_number}.json"
        )
    stops_json = json_data["MRData"]["RaceTable"]["Races"][0]["PitStops"]

    if fastest:
        ftime = min((i["duration"] for i in stops_json), key=get_sec)
        stops_json = [i for i in stops_json if i["duration"] == ftime]

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
    if year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )

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


def sprint_results(year: int, race_round: int):
    """Returns the sprint qualifying results for a year and round"""
    json_data = _get_json_content_from_url(
        f"http://ergast.com/api/f1/{year}/{race_round}/sprint.json"
    )
    if len(json_data["MRData"]["RaceTable"]["Races"]) == 0 :
        raise ValueError("No Sprint Race found for this Grand Prix")
    s_results = SprintResults(json_data["MRData"]["RaceTable"]["Races"][0]["SprintResults"])
    driver_pos = s_results.get_driver_pos()
    driver_name = s_results.get_driver_name()
    driver_team = s_results.get_driver_team()
    driver_status = s_results.get_driver_status()
    driver_number = s_results.get_driver_number()
    driver_laps = s_results.get_laps()
    driver_grid = s_results.get_driver_grid()
    driver_time = s_results.get_driver_time()
    driver_points = s_results.get_driver_points()

    return pd.DataFrame(
        zip(
            driver_pos, driver_name, driver_number, driver_team, driver_laps, driver_grid,
            driver_status, driver_time, driver_points
        ),
        columns=[
            "Position", "Name", "Driver Number", "Constructor", "Laps", "Grid",
            "Status", "Time", "Points"
        ]
    )


def get_constructors(year: Optional[int] = None):
    """Returns a list of constructors for a specified year"""
    if year is None:
        url = "https://ergast.com/api/f1/constructors.json?limit=230"
    elif year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )
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


def qualifying_results(year: int, race_round: int):
    """Returns the driver name , driver position, driver number, constructor name , the 3 Q times"""
    if year < 2003 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 2003 and {CURR_YEAR} are considered as valid value for year"
        )

    json_data = _get_json_content_from_url(
        f"https://ergast.com/api/f1/{year}/{race_round}/qualifying.json"
    )
    schedule_json = json_data["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"]
    r_obj = QualifyingResults(schedule_json)
    driver_positions = r_obj.get_positions()
    driver_names = r_obj.get_names()
    driver_numbers = r_obj.get_driver_numbers()
    constructor_names = r_obj.get_constructors()
    q1_times = r_obj.get_q1_times()
    q2_times = r_obj.get_q2_times()
    q3_times = r_obj.get_q3_times()
    return pd.DataFrame(
        zip(
            driver_positions,
            driver_names,
            driver_numbers,
            constructor_names,
            q1_times,
            q2_times,
            q3_times
        ),
        columns=[
            "Position",
            "DriverName",
            "DriverNumber",
            "Constructor",
            "Q1",
            "Q2",
            "Q3"
        ],
    )


def get_circuits(year: Optional[int] = None):
    """Returns the circuit name, circuit locality and circuit country"""
    if year is None:
        json_data = _get_json_content_from_url("http://ergast.com/api/f1/circuits.json?limit=100")
    elif year < 1950 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 1950 and {CURR_YEAR} are considered as valid value for year"
        )
    else:
        json_data = _get_json_content_from_url(f"https://ergast.com/api/f1/{year}/circuits.json")

    schedule_json = json_data["MRData"]["CircuitTable"]["Circuits"]
    rr_obj = RaceCircuits(schedule_json)
    circuit_name = rr_obj.get_circuit_name()
    circuit_locality = rr_obj.get_circuit_locality()
    circuit_country = rr_obj.get_circuit_country()
    return pd.DataFrame(
        zip(
            circuit_name,
            circuit_locality,
            circuit_country
        ),
        columns=[
            "Circuit",
            "Locality",
            "Country"
        ]
    )


def fastest_laps(year, race_round):
    """Returns the fastest lap for a particular race"""
    if year < 2004 or year > CURR_YEAR:
        raise ValueError(
            f"Only years between 2004 and {CURR_YEAR} are considered as valid value for year"
        )
    json_data = _get_json_content_from_url(
        f"https://ergast.com/api/f1/{year}/{race_round}/fastest/1/results.json"
    )
    races_json = json_data["MRData"]["RaceTable"]["Races"][0]["Results"][0]
    driver_id = races_json["Driver"]["driverId"]
    laps = races_json["laps"]

    json_data = _get_json_content_from_url(
        f"https://ergast.com/api/f1/{year}/{race_round}/drivers/{driver_id}/laps/{laps}.json"
    )
    timings_json = json_data["MRData"]["RaceTable"]["Races"][0]["Laps"][0]["Timings"][0]
    time = timings_json["time"]

    return pd.DataFrame(
        [[
            driver_id, laps, time
        ]],
        columns=[
            "Driver", "Laps", "Lap Time"
        ]
    )
