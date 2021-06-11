#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    uri = "wss://socket5.lichess.org/play/KvWAE1m2AIee/v6?sri=nmbWFJIm2ihm&v=0"
    async with websockets.connect(uri) as websocket:
        while True:
          res = await websocket.recv()
          print(res)

asyncio.get_event_loop().run_until_complete(hello())
