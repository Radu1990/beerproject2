import requests


# Requests commands

mainurl = 'http://localhost:5000/beercheck'

stuff = {"name": "Zaganu",
         "header": "New romanian IPA",
         "flavour": "Tastes good"}


def request_get(urlid=None):
    if urlid is not None:
        url_request = mainurl + ('/%s' % urlid)
    elif urlid is None:
        url_request = mainurl
    r = requests.get(url_request)
    print(url_request)
    print(r.status_code)


def request_put(urlid, data):
    url_request = mainurl + ('/%s' % urlid)

    r = requests.put(url_request, json=data)
    print(r.status_code)


def request_delete(urlid):
    url_request = mainurl + ('/%s' % urlid)
    r = requests.delete(url_request)
    print(r.status_code)


def request_post(data):
    url_request = mainurl
    r = requests.post(url_request, json=data)
    print(r.status_code)

# request_get()
# request_get(4)
# request_put(4, stuff)
# request_delete(4)
# request_post(stuff)


