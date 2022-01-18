from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.load("abhishek-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print("Retrieving initial value of favoriteNumber")
    stored_value = simple_storage.retrieve()
    print(stored_value)
    store_transactionn = simple_storage.store(190000, {"from": account})
    store_transactionn.wait(1)
    print("Retrieving updated value of favoriteNumber")
    stored_value = simple_storage.retrieve()
    print(stored_value)


def main():
    deploy_simple_storage()
