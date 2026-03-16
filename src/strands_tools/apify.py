"""Apify platform integration tool for Strands Agents.

Provides capabilities to run Apify Actors, retrieve Datasets, manage Key-Value Stores,
and interact with the Apify platform programmatically.

Environment variables:
    APIFY_API_TOKEN: Apify API token for authentication (required)
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
