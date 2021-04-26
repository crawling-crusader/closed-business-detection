import requests


url = "http://localhost:3001/places-api/stdcodes/"

def get_code(city):
    if is_alive():
        resp  = requests.get(url + city)
        print(resp.status_code)
        if resp.status_code == 200 and bool(resp.json()):
            return resp.json()[city.lower()]
    return "NotFound"


def is_alive():
    hcheck = requests.get(url + "Mumbai")
    if hcheck.status_code == 200:
        return True
    return False

def check_number():
    return None


if __name__== '__main__':
    res = get_code("af")
    print(res)