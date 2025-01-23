
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup 
import requests
# Helper Functions
def get_mvp_data(data, player):
    row = data[data['Player'] == player]
    if row.empty:
        print(f"No data found for player: {player}")
        return None
    
    row_array = np.asarray(row)[0]
    if any(pd.isna(row_array)):
        print(f"Invalid data for player: {player}, Data: {row_array}")
        return None

    try:
        numeric_indices = [i for i in range(4, 29)]  # Indices of numeric fields
        row_array = [
            float(row_array[i]) if i in numeric_indices else row_array[i]
            for i in range(len(row_array))
        ]
    except ValueError as e:
        print(f"Error converting player data to numeric: {e}")
        return None
    
    return row_array



def calculate_score(player_stats, team_stats):
    # print(player_stats)
    # print(player_stats[0], player_stats[28], player_stats[22], player_stats[23], player_stats[16])
    efg = player_stats[16] * 60
    stl = player_stats[24] * 10
    blk = player_stats[25] * 10
    rbs = player_stats[22] * 3
    ast = player_stats[23] * 3
    pts = player_stats[28] 
    rank = team_stats['Rank']
    wins = team_stats['Wins']
    score = (0.10 * (wins + rank)) + (0.28 * pts) + (0.12 * rbs) + (0.16 * ast) + (0.21 * efg) + (0.08 * (stl + blk))
    return round(score, 2)

def extract_team_info(row):
    try:
        team_name = row.find('a').text
        team_abbr = row.find('a')['href'].split('/')[-2].upper()
        wins = int(row.find('td', {'data-stat': 'wins'}).text)
        losses = int(row.find('td', {'data-stat': 'losses'}).text)
        win_loss_pct = row.find('td', {'data-stat': 'win_loss_pct'}).text
        return {
            'Team Name': team_name,
            'Team Abbreviation': team_abbr,
            'Wins': wins,
            'Losses': losses,
            'Win-Loss Percentage': win_loss_pct
        }
    except Exception as e:
        print(f"Error extracting team info: {e}")
        return None

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]['Wins'] > arr[j+1]['Wins']:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def get_team(all_teams, team_abb):
    for i in all_teams:
        if i['Team Abbreviation'] == team_abb:
            return i
    return None




def get_mvps(given_year):
    my_hash = {}
    url_player = "https://www.basketball-reference.com/awards/mvp.html"
    response_player = requests.get(url_player)
    response_player.encoding = 'utf-8'
    print("Response Status Code: ", response_player.status_code)

    soup = BeautifulSoup(response_player.text, 'html.parser')
    nba_winners = soup.find('table', {'id': 'mvp_NBA'})
    rows = nba_winners.find_all('tr')

    for row in rows[1:]:  # Skipping the first row which is usually the header
        columns = row.find_all('td')
        
        if len(columns) > 0:
            # Extract the year from the href attribute in the first column
            year_link = columns[0].find('a')['href']
            year = year_link.split('/')[-1].split('_')[1].split('.')[0]  # Extract year from URL
            player = columns[1].text.strip()  # Second column is the player name
            my_hash[year] = player
    return my_hash[given_year]