from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_with_link, get_account
from web3 import Web3


def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    creeation_tx = advanced_collectible.createCollectible({"from": account})
    creeation_tx.wait(1)
    print("Collectible created!")
