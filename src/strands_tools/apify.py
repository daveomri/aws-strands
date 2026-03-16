"""Apify platform integration tool for Strands Agents.

Provides capabilities to run Apify Actors, retrieve Datasets, manage Key-Value Stores,
and interact with the Apify platform programmatically.

Setup Requirements:
------------------
1. Create an Apify account at https://apify.com
2. Obtain your API token: Apify Console → Settings → API & Integrations → Personal API tokens
3. Set the environment variable:
   APIFY_API_TOKEN=your_api_token_here

Environment Variables:
    APIFY_API_TOKEN: Apify API token for authentication (required).
        Obtain from https://console.apify.com/settings/integrations

Example .env configuration:
    APIFY_API_TOKEN=apify_api_1a2B3cD4eF5gH6iJ7kL8m
"""

import logging

from strands_tools.utils import console_util

logger = logging.getLogger(__name__)
console = console_util.create()

try:
    from apify_client import ApifyClient  # noqa: F401

    HAS_APIFY_CLIENT = True
except ImportError:
    HAS_APIFY_CLIENT = False
