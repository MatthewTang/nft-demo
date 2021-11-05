# IPFS file management service
import os
from pathlib import Path
import requests

PINATA_BASE_URL = "https://api.pinata.cloud"
endpoint = "/pinning/pinFileToIPFS"

# filepath = "./img/pug.png"
filepath = "./front_end/src/img/luckin.png"
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


def upload_to_pinata(_filepath):
    with Path(_filepath).open("rb") as fp:
        img_binary = fp.read()
        _filename = _filepath.split("/")[-1:][0]
        res = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (_filename, img_binary)},
            headers=headers,
        )
        print(res.json())
        ipfs_hash = res.json()["IpfsHash"]
        image_url = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={_filename}"
        print(image_url)
        return image_url
