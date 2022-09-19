from bs4 import Tag

def get_constructors(table):
    teams_list = []
    for item in table:
        if isinstance(item, Tag):
            team_name = item.find("a", {"class": "dark bold uppercase ArchiveLink"})

            if team_name is not None:
                teams_list.append(team_name.decode_contents())

    return teams_list