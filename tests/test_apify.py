"""Tests for the Apify tool."""


def test_apify_module_is_importable():
    """Verify that the apify tool module can be imported from strands_tools."""
    from strands_tools import apify

    assert apify is not None
    assert apify.__name__ == "strands_tools.apify"
