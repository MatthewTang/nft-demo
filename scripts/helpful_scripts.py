from brownie import (
    network,
    accounts,
    config,
    LinkToken,
    VRFCoordinatorMock,
    Contract,
    interface,
)
from web3 import Web3


NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development"]
LOCAL_BLOCK_CHAIN = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + ["mainnet-fork"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"  # contract_adress and token id
BREED_MAPPING = {0: "PUG", 1: "SHIBA_INU", 2: "ST_BERNARD"}

contract_to_mock = {"link_token": LinkToken, "vrf_coordinator": VRFCoordinatorMock}

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def get_breed(id):
    return BREED_MAPPING[id]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)

    if network.show_active() in LOCAL_BLOCK_CHAIN:
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])


def get_contract(contract_name):
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deploy_mocks(decimals=18, initial_value=2000):
    print(f"the active network is {network.show_active}")
    print("deploying mocks...")
    account = get_account()
    print("deploying mock link token")
    link_token = LinkToken.deploy({"from": account})
    print(f"link token deployed to {link_token.address}")

    print("deploying mock vrfcoordinator")
    mock_vrf_coordinator = VRFCoordinatorMock.deploy(
        link_token.address, {"from": account}
    )
    print(f"VRFCoordinator deployed to {mock_vrf_coordinator.address}")

    print("Mocks deployed")


def fund_with_link(
    contract_address, account=None, link_token=None, amount=Web3.toWei(1, "ether")
):
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract("link_token")
    tx = interface.LinkTokenInterface(link_token).transfer(
        contract_address, amount, {"from": account}
    )
    print(f"funded {contract_address}")
    return tx
