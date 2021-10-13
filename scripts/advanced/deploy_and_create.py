from scripts.helpful_scripts import (
    OPENSEA_URL,
    get_account,
    get_contract,
    fund_with_link,
)
from brownie import AdvancedCollectible, config, network


def deploy_create():
    account = get_account()
    # Rinkeby
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("new token has been created!")


def main():
    deploy_create()
