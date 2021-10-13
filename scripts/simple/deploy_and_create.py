from scripts.helpful_scripts import OPENSEA_URL, get_account
from brownie import SimpleCollectible


sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"awesome, you can view your nft at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() -1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button.")