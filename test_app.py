from app import app as dash_app


def test_header_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_Region_filter_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region-filter", timeout=20)


def test_Chart_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#sales-chart", timeout=20)