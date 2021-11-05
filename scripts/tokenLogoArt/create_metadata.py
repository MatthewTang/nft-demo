import json
from pathlib import Path
from metadata.sample_metadat import metadata_template
from brownie import network

from scripts.upload_to_pinata import upload_to_pinata


name = "Luckin"
description = "A token for the luckin project"
filename = "luckin.json"
img_url = "https://ipfs.io/ipfs/QmWY2EYMpLsqWji6wwoToaXD2fBr7jMWavmFQjdhhVHtxQ?filename=luckin.png"


def main():
    metadata_file_name = f"./metadata/{network.show_active()}/{filename}"
    collectible_metadata = metadata_template
    print(metadata_file_name)
    if Path(metadata_file_name).exists():
        print(f"Metadata file {metadata_file_name} already exists.")
    else:
        print(f"Creating metadata file {metadata_file_name}")
        collectible_metadata["name"] = name
        collectible_metadata["description"] = description
        collectible_metadata["image"] = img_url

        with open(metadata_file_name, "w") as f:
            json.dump(collectible_metadata, f)
        upload_to_pinata(
            metadata_file_name,
        )
