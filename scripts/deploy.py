from brownie import accounts, config, network, SimpleStorage
import os


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print("Retrieving initial value of favoriteNumber")
    stored_value = simple_storage.retrieve()
    print(stored_value)
    store_transactionn = simple_storage.store(190000, {"from": account})
    store_transactionn.wait(1)
    print("Retrieving updated value of favoriteNumber")
    stored_value = simple_storage.retrieve()
    print(stored_value)


def get_account():
    # account = accounts[0]
    # account = accounts.load("abhishek-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
