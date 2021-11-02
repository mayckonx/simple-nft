from brownie import network, AdvancedCollectible
import pytest
import time
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
)
from scripts.advanced_collectible.deploy_and_create_advanced import deploy_and_create


def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for live testing")

    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(60)

    assert advanced_collectible.tokenCounter() == 1
