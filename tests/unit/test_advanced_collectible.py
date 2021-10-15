import pytest
from scripts.advanced.deploy_and_create import deploy_create
from scripts.advanced.set_tokenuri import set_tokenURI, dog_metadata_dic
from scripts.helpful_scripts import (
    LOCAL_BLOCK_CHAIN,
    get_account,
    get_contract,
    get_breed,
)

from brownie import network


def test_deploy_create_advanced_collectible():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() not in LOCAL_BLOCK_CHAIN:
        pytest.skip("Only for local testing")

    # Act
    advanced_collectible, creating_tx = deploy_create()
    requestId = creating_tx.events["requestedCollectible"]["requestId"]
    random_no = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_no, advanced_collectible.address, {"from": get_account()}
    )
    # assert
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_no % 3


def test_set_token_uri():
    # arrange
    if network.show_active() not in LOCAL_BLOCK_CHAIN:
        pytest.skip("only for local testing")

    advanced_collectible, creating_tx = deploy_create()
    requestId = creating_tx.events["requestedCollectible"]["requestId"]
    random_no = 777
    tx_callback = get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_no, advanced_collectible.address, {"from": get_account()}
    )
    tx_callback.wait(1)
    token_id = 0
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    token_uri = dog_metadata_dic[breed]
    # Act
    set_tokenURI(0, advanced_collectible, token_uri)
    assert advanced_collectible.tokenURI(token_id) == token_uri
