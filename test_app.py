from application import app
import json

# def test_quick():
#   a = "jeff"
#   greeting = greet(a)
#   assert greeting == "Hi jeff"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
def test_your_url():
    res = "http://deployment02-main-dev.us-east-2.elasticbeanstalk.com/gg"   # if we wanted to compare the result of the "shortened" url, this is what is should be
    response = app.test_client().post("/your-url", data={
        "code": "gg",
        "url": "http://wwww.google.com",
    })
    data = json.loads(response.get_data(as_text=True))
    with open("_resp.txt", "w") as file:
        file.write(data)
    assert response.status_code == 200    
