'''
Author: Farith Bascope
'''
import requests
from bs4 import BeautifulSoup

positions = ["S", #0-Safety
             "K", #1-Kicker
             "P", #2-Punter
             "T", #3-Tackle
             "C", #4-Center
             "G", #5-Guard
             "QB", #6-Quarterback
             "RB", #7-Running Back
             "WR", #8-Wide Receivers
             "TE", #9-Tight End
             "OL", #10-Offensive Line
             "DL", #11-Defensive Line
             "DT", #12-Defensive Tackle
             "DE", #13-Defensive End
             "LB", #14-LineBacker
             "LS", #15-Long Snapper
             "CB", #16-Corner Back
             "PK", #17-Punt Kicker
             "FB"  #18-Full Back
             ]

def scrape_table(t1, t2, desired_columns):
    result = []

    r1 = t1.find_all('tr')
    r2 = t2.find_all('tr')

    for row_1, row_2 in zip(r1, r2):
        cd1 = row_1.find_all(['td', 'th'])
        cd2 = row_2.find_all(['td', 'th'])

        data = [cell.get_text(strip=True) for idx, cell in enumerate(cd1 + cd2) if idx in desired_columns]
        if data[0] == '':
            continue
        if 0 in desired_columns:
            val = extract_positions(data[0])
            if not result and val == '':
                val = "Position"

            if val in data[0] and val != '':
                data[0] = data[0].rsplit(val, 1)[0].strip()
            data.append(val)
        result.append(data)
    return result


def extract_positions(entry):
    extracted_positions = ''

    # positions = [
    #     "S", "K", "P", "T", "C", "G", "QB", "RB", "WR", "TE", "OL", "DL", "DT", "DE", "LB", "LS", "CB", "PK", "FB"
    #     # if single character add to the start of the list, if 2 character add anywhere in the middle,
    #     # if three character add to the last. I.E add based on the position value character length
    # ]

    for position in positions:
        if entry.endswith(position):
            extracted_positions = position

    return extracted_positions


def init(url_init):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    html_source = requests.get(url_init, headers=headers).text

    if html_source:
        soup = BeautifulSoup(html_source, 'html.parser')
        table_columns = [
            [0, 5, 9],
            [0, 3, 7],
            [0, 2, 4, 6],
            [0, 4, 5, 9, 14, 16],
            [],  # do not remove these blank ones
            [],  # do not remove these blank ones
            [0, 2, 3, 13],
            [],  # do not remove these blank ones
        ]

        combined_tables = []

        tables = soup.find_all('table')
        for i in range(0, len(tables) - 1, 2):
            table1 = tables[i]
            table2 = tables[i + 1]
            desired_columns = table_columns[i // 2] if i // 2 < len(table_columns) else []
            if not desired_columns:
                continue
            combined_tables.append(scrape_table(table1, table2, desired_columns))

        # for idx, table_data in enumerate(combined_tables):
        #     print(f"Table {idx + 1}:")
        #     for row_data in table_data:
        #         print(row_data)
        #     print()

        return combined_tables
    else:
        return 0;


if __name__ == "__main__":
    #url = "https://www.espn.com/nfl/team/stats/_/name/buf/buffalo-bills"
    #url = "https://www.espn.com/nfl/team/stats/_/name/ne/new-england-patriots"
    url = "https://www.espn.com/nfl/team/stats/_/name/ari/arizona-cardinals"
    init(url)