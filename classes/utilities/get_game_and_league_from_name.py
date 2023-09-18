from classes.firebase.firebase_league_names import get_league_name_info


def get_league_and_game_id_from_league_name(league_name):

    all_leagues = get_league_name_info()
    league_info = all_leagues[league_name]
    league_id = str(league_info['league_id'])
    game_id = str(league_info['game_id'])

    return game_id, league_id
