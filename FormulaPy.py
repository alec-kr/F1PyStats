from copyreg import constructor
import requests
import pandas as pd

import bs4
from bs4 import BeautifulSoup

def driver_standings():
    page = requests.get("https://www.formula1.com/en/results.html/2022/drivers.html")

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

def constructor_standings():
    page = requests.get("https://www.formula1.com/en/results.html/2022/team.html")

    soup = BeautifulSoup(page.content, 'html.parser')
    name_info = soup.find_all("table", {"class": "resultsarchive-table"})

    table = []
    table = name_info[0].findChildren("tr")

    positions = get_positions(table)
    teams = get_constructors(table)
    points = get_points(table)

    wcc_df = pd.DataFrame(list(zip(positions, teams, points)), columns=["POS","Constructor","Points"])

    return wcc_df

def race_results(year):
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


def get_names(table):
    names_list = []
    for item in table:
        if isinstance(item, bs4.Tag):
            f_name = item.find("span", {"class": "hide-for-tablet"})
            l_name = item.find("span", {"class": "hide-for-mobile"})

            if f_name is not None and l_name is not None:
                names_list.append(f_name.decode_contents() + " " + l_name.decode_contents())

    return names_list

def get_driver_teams(table):
    teams_list = []
    for item in table:
        if isinstance(item, bs4.Tag):
            team_name = item.find("a", {"class": "grey semi-bold uppercase ArchiveLink"})

            if team_name is not None:
                teams_list.append(team_name.decode_contents())

    return teams_list

def get_constructors(table):
    teams_list = []
    for item in table:
        if isinstance(item, bs4.Tag):
            team_name = item.find("a", {"class": "dark bold uppercase ArchiveLink"})

            if team_name is not None:
                teams_list.append(team_name.decode_contents())

    return teams_list

def get_winning_constructors(table):
    teams_list = []
    for item in table:
        if isinstance(item, bs4.Tag):
            team_name = item.find("td", {"class": "semi-bold uppercase"})

            if team_name is not None:
                teams_list.append(team_name.decode_contents())

    return teams_list

def get_points(table):
    points_list = []
    for item in table:
        if isinstance(item, bs4.Tag):
            curr_points = item.find("td", {"class": "dark bold"})

            if curr_points is not None:
                points_list.append(curr_points.decode_contents())

    return points_list

def get_positions(table):
    positions_list = []
    for item in table:
        if isinstance(item, bs4.Tag):
            position = item.find("td", {"class": "dark"})

            if position is not None:
                positions_list.append(position.decode_contents())
    
    return positions_list

def get_nationalities(table):
    nationality_list = []
    for item in table:
        if isinstance(item, bs4.Tag):
            nationality = item.find("td", {"class": "dark semi-bold uppercase"})

            if nationality is not None:
                nationality_list.append(nationality.decode_contents())
    
    return nationality_list

def get_grands_prix(table):
    gps = []
    for item in table:
        if isinstance(item, bs4.Tag):
            gp_name = item.find("a", {"class": "dark bold ArchiveLink"})

            if gp_name is not None:
                gp_name = gp_name.decode_contents()
                gps.append(" ".join(gp_name.split()))
    
    return gps

def get_race_dates(table):
    race_dates = []
    for item in table:
        if isinstance(item, bs4.Tag) and item is not None:
            date = item.find("td", {"class": "dark hide-for-mobile"})

            if date is not None:
                race_dates.append(date.decode_contents())
    
    return race_dates

def get_race_laps(table):
    race_laps = []
    for item in table:
        if isinstance(item, bs4.Tag) and item is not None:
            laps = item.find("td", {"class": "bold hide-for-mobile"})

            if laps is not None:
                race_laps.append(laps.decode_contents())
    
    return race_laps

def get_race_time(table):
    race_times = []
    for item in table:
        if isinstance(item, bs4.Tag) and item is not None:
            time = item.find("td", {"class": "dark bold hide-for-tablet"})

            if time is not None:
                race_times.append(time.decode_contents())
    
    return race_times


# print(driver_standings())
# print(constructor_standings())
print(race_results(2022))