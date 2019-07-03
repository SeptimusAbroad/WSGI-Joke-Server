from wsgiref.simple_server import make_server
import requests
import random


def dadjoke3000():
    """This function calls out to the icanhazdadjoke.com API and shoots out a GET request. It then stores the results
    in a local variable and encodes them into a bytestring format contained in a list for display on an HTML page."""
    url = "https://icanhazdadjoke.com/search"
    search = ""
    response = requests.get(url, headers={"Accept": "application/json"}, params={"term": search})
    data = response.json()
    results = (data['results'])
    amount1 = (len(data['results']))
    amount2 = amount1 - 1
    response1 = (results[random.randint(0, amount2)]["joke"])
    jokes = f"<h1>I have a random dad joke for you! Here's one: {response1}</h1>"
    return [jokes.encode('utf-8')]


def main():
    """This "web_app" as it is, is a one half of the required pieces you need to run the simple server. It sets up
    the basic skeleton of what is displayed on the HTML page."""
    def web_app(environment, response):
        status = "200 OK"
        headers = [("Content-type", "text/html; charset=utf-8")]
        response(status, headers)
        return dadjoke3000()

    """And here it is! The simple server. This is the meat-and-potatoes. It sets up a server running on port 8080 and
    gets it running in perpetuity."""
    with make_server("", 8080, web_app) as server:
        print("serving on port 8080 \nVisit http://localhost:8080/dad-jokes\n")
        server.serve_forever()


if __name__ == "__main__":
    main()
