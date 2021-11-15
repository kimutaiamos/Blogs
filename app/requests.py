import requests
from sqlalchemy.engine import url

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    """
    function that consumes the quotes api
    """

    response = requests.get(url).json()

    random_quote =(response.get("author"),response.get("quote"))
    return random_quote