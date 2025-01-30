import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
@pytest.fixture
def app_runner(dash_duo):
    app = import_app("app")
    return dash_duo.start_server(app)

def test_header_is_present(dash_duo):

    header = dash_duo.find_element('header')
    assert header is not None, "Header element not found"

def test_visualization_present(dash_duo):
    visualization = dash_duo.find_element('visualization')
    assert visualization is not None, "Visualization is not present"

def test_region_picker_present(dash_duo):
    region_picker = dash_duo.find_element('region-picker')
    assert region_picker is not None, "Region picker is not present"
