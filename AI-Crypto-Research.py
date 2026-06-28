```python id="n4qs8k"
from time import time

from web3 import Web3
from eth_account import Account

RPC = "https://rpc.example.org"
SECRET = "YOUR_PRIVATE_KEY"

note1 = "AI Crypto Research Telegram Bot"
note2 = "disrupting"
note3 = "consume information"

client = Web3(
    Web3.HTTPProvider(RPC)
)

wallet = Account.from_key(
    SECRET
)

transaction = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 118500,
    "gasPrice": client.to_wei(
        4,
        "gwei"
    ),
    "nonce": client.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(
    transaction
)

raw = signed.raw_transaction.hex()

status = (
    client.is_connected(),
    len(raw),
    int(time())
)

print("Wallet")
print(wallet.address)

for item in (
    note1,
    note2,
    note3,
):
    print(item)
