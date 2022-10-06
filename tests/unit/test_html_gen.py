import os 
from pycribbage import html_gen
def test_html_gen_load_json():
    return
    data = html_gen.load_json(os.path.join('tests','example_state.json')) 
    
    keys=['p1_score']
    for key in keys:
        assert key in data.keys()

def test_html_gen_update_template():
    pass
