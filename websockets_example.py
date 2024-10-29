"""Example for connecting to private WebSockets with an existing account.

Usage: python -m examples.websockets
"""

import asyncio
import json
import websockets

from dydx3.helpers.request_helpers import generate_now_iso
from dydx3.constants import WS_HOST_SEPOLIA


now_iso_string = generate_now_iso()

req = {
    "type": "subscribe",
    "channel": "v3_accounts",
    "accountNumber": "0",
    "apiKey": "51b77d77d5de0132f3b3bb897ab2c438",
    "passphrase": "passphrase",
    "timestamp": now_iso_string,
    "signature": "signature",
}


async def main():
    async with websockets.connect(WS_HOST_SEPOLIA+"/accounts") as websocket:

        await websocket.send(json.dumps(req))
        print(f"> {req}")

        while True:
            res = await websocket.recv()
            print(f"< {res}")


asyncio.get_event_loop().run_until_complete(main())
