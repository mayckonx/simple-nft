import os, requests
from pathlib import Path

PINATA_BASE_URL = "https://api.pinata.cloud/"
ENDPOINT = "pinning/pinFileToIPFS"
FILEPATH = "./img/pug.png"
FILENAME = FILEPATH.split("/")[-1:][0]
HEADERS = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def main():
    with Path(FILEPATH).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + ENDPOINT,
            files={"file": (FILENAME, image_binary)},
            headers=HEADERS,
        )
        print(response.json())
