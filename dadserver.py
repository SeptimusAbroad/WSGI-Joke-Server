from wsgiref.simple_server import make_server
import requests
import random

def dadjoke3000():
    url = "https://icanhazdadjoke.com/search"
    search = ""
    response = requests.get(url, headers={"Accept": "application/json"}, params={"term": search})
    data = response.json()
    results = (data['results'])
    amount1 = (len(data['results']))
    amount2 = amount1 - 1
    response1 = (results[random.randint(0, amount2)]["joke"])
    jokes = (f"<h1>I have a random dad joke for you! Here's one: {response1}</h1>")
    return [jokes.encode('utf-8')]


def main():
    def web_app(environment, response):
        status = "200 OK"
        headers = [("Content-type", "text/html; charset=utf-8")]
        response(status, headers)
        return dadjoke3000()


    with make_server("", 8080, web_app) as server:
        print("serving on port 8080 \nVisit http://localhost:8080/dad-jokes\n")
        server.serve_forever()


if __name__ =="__main__":
    main()
