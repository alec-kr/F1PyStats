from bs4 import Tag

# Return the constructor names from the table
def get_constructors(table, page):
    teams_list = []
    for item in table:
        team_name = ""
        if isinstance(item, Tag):
            if page == "team_standings":
                team_name = item.find("a", {"class": "dark bold uppercase ArchiveLink"})
            
            elif page == "fastest_lap":
                team_name = item.find("td", {"class": "width25 semi-bold uppercase"})
            
            elif page == "race_results":
                team_name = item.find("td", {"class": "semi-bold uppercase"})
            
            elif page == "drivers_results":
                team_name = item.find("a", {"class": "grey semi-bold uppercase ArchiveLink"})

            if team_name is not None:
                teams_list.append(team_name.decode_contents())

    return teams_list