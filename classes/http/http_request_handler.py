import logging
import requests

query_params = {'format': 'json'}
logger = logging.getLogger(__name__)


def make_api_call(url_to_call, access_token):

    logger.debug('URL Endpoint: ' + url_to_call)
    bearer_string = 'Bearer ' + access_token
    headers = {'Authorization': bearer_string, 'Accept-Encoding': 'gzip, deflate, br',
               'Accept': '*/*'}
    params = {'format': 'xml'}

    try:
        game_id = requests.get(url=url_to_call, headers=headers, params=params,
                               stream=True)
        if 199 <= game_id.status_code < 300:
            xml_content = game_id.content
            xml_to_parse = xml_content.decode('utf-8')
            return xml_to_parse
        else:
            logger.error('HTTP Error - Code: ' + str(game_id.status_code))
            return "ERROR"
    except requests.HTTPError as error:
        logger.error('rest_call_handler.py - make_api_call - Error: ' + str(error))
        return str(error.response.status_code)
