from app.controllers import application_controller as app_controller

def test_webapp_index():
    response = app_controller.index()
    content = response.body.read().decode('utf-8')
    assert response.status_code == 200
    assert 'welcome.jpg' in content
