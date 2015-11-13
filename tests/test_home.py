from mentorfy.controllers import home

def test_webapp_index():
    content = home.index()
    assert 'welcome.jpg' in content
