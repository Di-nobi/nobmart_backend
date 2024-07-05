from web3 import Web3
from app.config import INFURA_PROJECT_ID

web3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))
contract_address = ""
contract_abi = []
contract = web3.eth.contract(address=web3.to_checksum_address(contract_address), abi=contract_abi)

def get_balance(address:str):
    main_balance = web3.eth.get_balance(address)
    return web3.from_wei(main_balance, 'ether')


def create_transaction(wallet_address:str, private_key: str, value: str):
    nonce = web3.eth.get_transaction_count(wallet_address)
    gas_price = web3.eth.gas_price
    gas_limit = 30000
    to_address = web3.to_checksum_address(contract_address)
    value = web3.to_wei(value, 'ether')
    tx = contract.functions.transfer(to_address, value).build_transaction({
        'nonce': nonce,
        'gasPrice': gas_price,
        'gas': gas_limit
    })
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    return tx_hash.hex()