from enum import Enum


# Consolidated all the URLs into a single location for easier maintenance.
class UrlTemplate(Enum):

    # Base URL for all API calls
    BASE_API_URL = 'https://fantasysports.yahooapis.com/fantasy/v2'

    # League Settings URLs - Gets Points for Calculations
    LEAGUE_SETTINGS_LOADER = '/league/{game_id}.l.{league_id}/settings'
