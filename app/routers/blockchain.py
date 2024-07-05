# from fastapi import APIRouter, HTTPException
# from app.utils.blockchain import get_balance, create_transaction
# from app.schemas import WalletConnectRequest, Wallet, TransactionRequest
# router = APIRouter()

# @router.post('/connect_wallet')
# def connect_wallet(request: WalletConnectRequest):
#     balance = get_balance(request.address)
#     if  balance is None:
#         raise HTTPException(status_code=400, detail='Invalid wallet address')
#     return {'balance': balance}

# @router.post('/create_transaction')
# def create_transaction(request: TransactionRequest):
#     tx_hash = create_transaction(request.wallet_address, request.private_key, request.value)
#     return {'tx_hash': tx_hash}