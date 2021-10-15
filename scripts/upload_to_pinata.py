# IPFS file management service
import os
from pathlib import Path
import requests

PINATA_BASE_URL = "https://api.pinata.cloud"
endpoint = "/pinning/pinFileToIPFS"

filepath = "./img/pug.png"
filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def main():
    with Path(filepath).open("rb") as fp:
        img_binary = fp.read()
        res = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, img_binary)},
            headers=headers,
        )
        print(res.json())
