import requests

def make_request(url):
    url = url

    headers = {
        'auth': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUwNCwiaWRlbiI6IjI1OTQ0NTg1MTQzMTIzOTY5MSIsIm1kIjp7fSwidHMiOjE1NTQ5MjY4NDE2ODJ9.xSjEv4wdLMNSujYQIqw1j7jFC1F61fj0PnDinFT_5o4"
        }

    response = requests.request("GET", url, headers=headers)

    data = response.json()
    return data

# Notable player IDS:
# Me: 98Y2CVV8
# LucasXGamer CR (Good 2.6 Hog player): 9G28ULYR 
data = make_request("https://api.royaleapi.com/player/98Y2CVV8/battles")
data
