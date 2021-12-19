from brownie import accounts, SimpleStorage, network, config
import os

def deploy_simple_storage():
  account = get_account()
  simple_storage = SimpleStorage.deploy({"from": account})
  print(simple_storage)
  stored_value = simple_storage.retrieve()
  print(stored_value)
  transaction = simple_storage.store(15, {"from": account})
  transaction.wait(1)
  updated_stored_value = simple_storage.retrieve()
  print(updated_stored_value)
  # pass
  # account = accounts.load('development-account')
  # print(account)

def get_account():
  if network.show_active() == "developement":
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])

def main():
  print(os.getenv("WEB3_INFURA_PROJECT_ID"))
  deploy_simple_storage()