import pytest
from scripts.helpful_scripts import LOCAL_BLOCK_CHAIN, get_account
from scripts.deploy_and_create import sample_token_uri
from brownie import network, SimpleCollectible


def test_deploy_create_collectible():
    if network.show_active() not in LOCAL_BLOCK_CHAIN:
        pytest.skip()

    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    assert simple_collectible.ownerOf(0) == get_account()
