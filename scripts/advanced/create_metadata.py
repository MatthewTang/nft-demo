from typing import no_type_check_decorator
from brownie import AdvancedCollectible, network

from scripts.helpful_scripts import get_breed
from metadata.sample_metadat import metadata_template
from pathlib import Path
import requests
import json
import os

breed_to_image_uri = {
    "PUB": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA-INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}


def main():
    advanced_collectible = AdvancedCollectible[-1]
    no_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"you have created {no_advanced_collectibles} collectibles")
    for token_id in range(no_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        print(metadata_file_name)
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} alrdy exists ! Delete it to overwrite")
        else:
            print(f" create metadata file: {metadata_file_name} ")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An aborable {breed}"
            image_path = (
                f'./img/{breed.lower().replace("_","-")}.png'  # './img/shiba-inu.png'
            )

            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_url = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else breed_to_image_uri[breed]
            collectible_metadata["image"] = image_url

            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(file_path):
    with Path(file_path).open("rb") as fp:
        img_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        res = requests.post(f"{ipfs_url}{endpoint}", files={"file": img_binary})
        ipfs_hash = res.json()["Hash"]
        # "./img/shiba-inu.png" -> "shiba-inu.png"
        filename = file_path.split("/")[-1:][0]
        image_url = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_url)
        return image_url
