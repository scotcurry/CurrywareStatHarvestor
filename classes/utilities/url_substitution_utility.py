def build_url(url_to_modify, game_id, league_id):

    if 'game_id' in url_to_modify:
        url_to_modify = url_to_modify.replace('{game_id}', game_id)
    if 'league_id' in url_to_modify:
        url_to_modify = url_to_modify.replace('{league_id}', league_id)

    return url_to_modify
