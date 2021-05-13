def contender(date):
    import pandas as pd
    import time
    from datetime import datetime, timedelta
    from nba_api.stats.endpoints import scoreboardv2

    #initialize
    standings = scoreboardv2.ScoreboardV2(game_date = date)
    ec_standings = standings.get_data_frames()[4]
    wc_standings = standings.get_data_frames()[5]
    standings_df = pd.concat([ec_standings, wc_standings], axis = 0, ignore_index = True)
    teams_list = list(standings_df['TEAM'])
    contender = {}
    new_teams_list = [i for i in teams_list]

    while len(new_teams_list) > 0:
        for team in teams_list:
            if (standings_df.loc[standings_df['TEAM'] == team]['W'] >= 40).all() and (standings_df.loc[standings_df['TEAM'] == team]['L'] < 20).all():
                contender[team] = True
                new_teams_list.remove(team)
            elif (standings_df.loc[standings_df['TEAM'] == team]['L'] >= 20).all() and (standings_df.loc[standings_df['TEAM'] == team]['W'] < 40).all():
                contender[team] = False
                new_teams_list.remove(team)

        teams_list = [i for i in new_teams_list]
        date = datetime.strptime(date, '%Y-%m-%d') + timedelta(days = 1)
        date = datetime.strftime(date, '%Y-%m-%d')
        time.sleep(3)     # Need to sleep to avoid over accessing nba_api
        standings = scoreboardv2.ScoreboardV2(game_date = date)
        ec_standings = standings.get_data_frames()[4]
        wc_standings = standings.get_data_frames()[5]
        standings_df = pd.concat([ec_standings, wc_standings], axis = 0, ignore_index = True)
        
    return contender
