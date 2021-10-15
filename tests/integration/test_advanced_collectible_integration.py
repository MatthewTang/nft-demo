import pytest
from scripts.advanced.deploy_and_create import deploy_create
from scripts.helpful_scripts import LOCAL_BLOCK_CHAIN
from brownie import network
import time


def test_deploy_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() in LOCAL_BLOCK_CHAIN:
        pytest.skip("Only for integration testing")

    # Act
    advanced_collectible, _ = deploy_create()
    time.sleep(600)
    # assert
    assert advanced_collectible.tokenCounter() == 1
