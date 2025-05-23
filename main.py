import asyncio
import threading
from ui.interface import TradeSimulatorUI
from websocket.client import WebSocketClient

def run_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == "__main__":
    app = TradeSimulatorUI()

    # Callback function to update UI thread-safely
    def update_ui(text):
        app.after(0, app.update_output, text)

    # Initialize WebSocket client with default symbol
    ws_client = WebSocketClient(symbol="BTC-USDT-SWAP", ui_callback=update_ui)

    # Start asyncio event loop in a separate thread
    loop = asyncio.new_event_loop()
    threading.Thread(target=run_event_loop, args=(loop,), daemon=True).start()

    # Schedule websocket client connection in event loop
    asyncio.run_coroutine_threadsafe(ws_client.connect(), loop)

    app.mainloop()

    # On app close, stop WebSocket client and event loop
    ws_client.stop()
    loop.call_soon_threadsafe(loop.stop)
