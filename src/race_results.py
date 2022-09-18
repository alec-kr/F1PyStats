from bs4 import Tag

def get_winning_constructors(table):
    teams_list = []
    for item in table:
        if isinstance(item, Tag):
            team_name = item.find("td", {"class": "semi-bold uppercase"})

            if team_name is not None:
                teams_list.append(team_name.decode_contents())

    return teams_list

def get_grands_prix(table):
    gps = []
    for item in table:
        if isinstance(item, Tag):
            gp_name = item.find("a", {"class": "dark bold ArchiveLink"})

            if gp_name is not None:
                gp_name = gp_name.decode_contents()
                gps.append(" ".join(gp_name.split()))
    
    return gps

def get_race_dates(table):
    race_dates = []
    for item in table:
        if isinstance(item, Tag) and item is not None:
            date = item.find("td", {"class": "dark hide-for-mobile"})

            if date is not None:
                race_dates.append(date.decode_contents())
    
    return race_dates

def get_race_laps(table):
    race_laps = []
    for item in table:
        if isinstance(item, Tag) and item is not None:
            laps = item.find("td", {"class": "bold hide-for-mobile"})

            if laps is not None:
                race_laps.append(laps.decode_contents())
    
    return race_laps

def get_race_time(table):
    race_times = []
    for item in table:
        if isinstance(item, Tag) and item is not None:
            time = item.find("td", {"class": "dark bold hide-for-tablet"})

            if time is not None:
                race_times.append(time.decode_contents())
    
    return race_times