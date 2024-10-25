from datetime import datetime, timedelta
from dydx3 import Client
from dydx3.constants import API_HOST_SEPOLIA, NETWORK_ID_SEPOLIA, MARKET_BTC_USD, ORDER_SIDE_SELL, ORDER_TYPE_LIMIT
import random

Private = "0x294b64d3b8dd640c7c87520e8b49bac734aa27f65e921bf94c9f1ff54a2fd9f"
Public = "0x377b464e991591aeabadc7923d4fa8618979bd4157d90115fbb62cbb74169c9"

private_client = Client(
    host=API_HOST_SEPOLIA,
    stark_private_key=Private,
    stark_public_key=Public,
    api_key_credentials={
        "secret": "anything",
        "key": "51b77d77d5de0132f3b3bb897ab2c438",
        "passphrase": "anything",
    },
    network_id=NETWORK_ID_SEPOLIA,
)

orderbook_expire = datetime.now() + timedelta(days=1)
order_response = private_client.private.create_order(
    103883,
    MARKET_BTC_USD,
    ORDER_SIDE_SELL,
    ORDER_TYPE_LIMIT,
    False,
    "0.001",
    "69500.0",
    "0.001",
    expiration_epoch_seconds=int(orderbook_expire.timestamp()),
    client_id=f"{random.randint(0, 1000000)}",
)

print(order_response.data)

print(private_client.private.get_accounts().data)
print(private_client.private.get_positions().data)
print(private_client.private.get_orders().data)
print(private_client.private.get_fills().data)
