import xml.etree.ElementTree as ET

from classes.firebase.firebase_get_oauth_token import get_oauth_token

from classes.fantasy.url_templates import UrlTemplate

from classes.http.http_request_handler import make_api_call

from classes.utilities.url_substitution_utility import build_url
from classes.utilities.get_game_and_league_from_name import \
    get_league_and_game_id_from_league_name


def get_league_settings_json(league_name):

    game_id, league_id = get_league_and_game_id_from_league_name(league_name)
    base_url = UrlTemplate.BASE_API_URL.value
    league_settings_endpoint = UrlTemplate.LEAGUE_SETTINGS_LOADER.value
    url_to_modify = base_url + league_settings_endpoint
    url_to_call = build_url(url_to_modify, game_id, league_id)
    access_token = get_oauth_token()
    settings_xml = make_api_call(url_to_call, access_token)
    data_to_parse = prep_return_data(settings_xml)
    settings_dict = parse_xml_to_stats_dict(data_to_parse)
    settings_to_return = {'score_settings': settings_dict}

    return settings_to_return


def parse_xml_to_stats_dict(data_to_parse):

    root = ET.fromstring(data_to_parse)
    stat_category_node = root.findall('./league/settings/stat_categories/stats/stat')
    all_settings = []
    counter = 0
    while counter < len(stat_category_node):
        current_stat = stat_category_node[counter]
        counter = counter + 1
        stat_id = current_stat.find('./stat_id').text
        stat_enabled = current_stat.find('./enabled').text
        stat_name = current_stat.find('./name').text
        display_name = current_stat.find('./display_name').text
        query_string = ("./league/settings/stat_modifiers/stats/stat[stat_id='"
                        + stat_id + "']")
        stat_mod_node = root.find(query_string)
        stat_mod_value = None
        if stat_mod_node is not None:
            stat_mod_value = stat_mod_node.find('./value').text

        stat_dict = {'stat_enabled': stat_enabled, 'display_name': display_name,
                     'stat_value': stat_mod_value, 'stat_name': stat_name,
                     'stat_id': stat_id}

        all_settings.append(stat_dict)

    return all_settings


def prep_return_data(settings_xml):
    search_from_here = settings_xml.find('copyright')
    closing_bracket = settings_xml.find('>', search_from_here)
    total_length = len(settings_xml)
    second_part = settings_xml[closing_bracket: total_length]

    return '<fantasy_content' + second_part
