from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected_value = 5

    # Assert
    assert starting_value == expected_value


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    expected_value = 100
    store_txn = simple_storage.store(100)
    stored_value = simple_storage.retrieve()

    # Assert
    assert stored_value == expected_value
