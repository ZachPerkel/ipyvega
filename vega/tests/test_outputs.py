import pytest

import pandas as pd

from .. import Vega, VegaLite


PANDAS_DATA = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
JSON_DATA = {
    "values": [
        {"x": 1, "y": 4},
        {"x": 2, "y": 5},
        {"x": 3, "y": 6}
    ]
}

VEGALITE_SPEC = {
    "mark": "circle",
    "encoding": {
        "x": {"field": "x", "type": "quantitative"},
        "y": {"field": "y", "type": "quantitative"}
    }
}

# TODO: use an actual Vega spec
VEGA_SPEC = VEGALITE_SPEC


def test_vegalite_output():
    # TODO: somehow test that output is valid HTML/JS?
    spec_with_data = VEGALITE_SPEC.copy()
    spec_with_data['data'] = JSON_DATA

    # Test three ways of specifying data
    obj1 = VegaLite(VEGALITE_SPEC, PANDAS_DATA)
    obj2 = VegaLite(VEGALITE_SPEC, JSON_DATA['values'])
    obj3 = VegaLite(spec_with_data)

    html1 = obj1._generate_html(id='ABC')
    html2 = obj2._generate_html(id='ABC')
    html3 = obj3._generate_html(id='ABC')
    assert html1 == html2 == html3

    js1 = obj1._generate_js(id='ABC', sort_keys=True)
    js2 = obj2._generate_js(id='ABC', sort_keys=True)
    js3 = obj3._generate_js(id='ABC', sort_keys=True)
    assert js1 == js2 == js3

    # Check for error when no data is provided
    with pytest.raises(ValueError) as err:
        VegaLite(VEGALITE_SPEC)
    assert str(err.value) == 'No data provided'


def test_vega_output():
    # TODO: use an actual vega spec
    data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    obj = Vega(VEGA_SPEC, data)
    html = obj._generate_html(id='ABC')
    js = obj._generate_js(id='ABC')
