import asyncio
import json
import time
import logging
from utils.latency import measure_latency  # we'll create this next
from models.slippage import estimate_slippage  # placeholder imports for model functions
from models.fees import estimate_fees
from models.market_impact import calculate_market_impact
from models.maker_taker import predict_maker_taker

logger = logging.getLogger(__name__)

class WebSocketClient:
    def __init__(self, symbol, ui_callback):
        self.url = f"wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/{symbol}"
        self.ui_callback = ui_callback  # function to update UI output
        self.running = False

    async def connect(self):
        import websockets
        self.running = True
        async with websockets.connect(self.url) as ws:
            logger.info(f"Connected to {self.url}")
            while self.running:
                try:
                    msg = await ws.recv()
                    tick_data = json.loads(msg)
                    start = time.perf_counter()
                    output_text = self.process_tick(tick_data)
                    latency = (time.perf_counter() - start) * 1000  # ms
                    output_text += f"\nInternal Latency: {latency:.2f} ms\n"
                    self.ui_callback(output_text)
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    await asyncio.sleep(1)

    def process_tick(self, tick_data):
        # Extract relevant info from tick_data
        asks = tick_data.get("asks", [])
        bids = tick_data.get("bids", [])
        quantity = 100  # fixed or fetch from UI input
        volatility = 0.05  # placeholder, replace with actual value
        fee_tier = "Tier 1"  # placeholder

        # Call model functions (implement these later)
        slippage = estimate_slippage(asks, bids, quantity, volatility)
        fees = estimate_fees(quantity, fee_tier)
        market_impact = calculate_market_impact(quantity, volatility, bids)
        maker_taker = predict_maker_taker(asks, bids, quantity)

        # Compose output string
        output = (
            f"Expected Slippage: {slippage:.6f}\n"
            f"Expected Fees: {fees:.6f}\n"
            f"Market Impact: {market_impact:.6f}\n"
            f"Net Cost: {slippage + fees + market_impact:.6f}\n"
            f"Maker/Taker Proportion: {maker_taker:.2%}\n"
        )
        return output

    def stop(self):
        self.running = False
