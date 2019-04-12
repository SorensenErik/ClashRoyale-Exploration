import http.client

conn = http.client.HTTPConnection("api.royaleapi.com")

headers = {
    'auth': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUwNCwiaWRlbiI6IjI1OTQ0NTg1MTQzMTIzOTY5MSIsIm1kIjp7fSwidHMiOjE1NTQ5MjY4NDE2ODJ9.xSjEv4wdLMNSujYQIqw1j7jFC1F61fj0PnDinFT_5o4",
    }

conn.request("GET", "/top/players/", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
