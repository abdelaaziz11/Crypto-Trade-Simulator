import tkinter as tk
from tkinter import ttk

class TradeSimulatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Real-Time Crypto Trade Simulator")
        self.geometry("900x500")
        self.create_widgets()

    def create_widgets(self):
        # Left Panel - Inputs
        left_frame = ttk.Frame(self, padding=10, width=300)
        left_frame.pack(side="left", fill="y")

        ttk.Label(left_frame, text="Input Parameters", font=("Helvetica", 16)).pack(pady=10)

        # Exchange Dropdown
        ttk.Label(left_frame, text="Exchange:").pack(anchor="w")
        self.exchange_var = tk.StringVar(value="OKX")
        exchange_dropdown = ttk.Combobox(left_frame, textvariable=self.exchange_var, state="readonly")
        exchange_dropdown['values'] = ["OKX"]
        exchange_dropdown.pack(fill="x", pady=5)

        # Spot Asset Dropdown
        ttk.Label(left_frame, text="Spot Asset:").pack(anchor="w")
        self.asset_var = tk.StringVar(value="BTC-USDT-SWAP")
        asset_dropdown = ttk.Combobox(left_frame, textvariable=self.asset_var)
        asset_dropdown['values'] = ["BTC-USDT-SWAP", "ETH-USDT-SWAP", "LTC-USDT-SWAP"]
        asset_dropdown.pack(fill="x", pady=5)

        # Order Type (fixed)
        ttk.Label(left_frame, text="Order Type:").pack(anchor="w")
        self.order_type_var = tk.StringVar(value="Market")
        order_type_entry = ttk.Entry(left_frame, textvariable=self.order_type_var, state="readonly")
        order_type_entry.pack(fill="x", pady=5)

        # Quantity
        ttk.Label(left_frame, text="Quantity (USD Equivalent):").pack(anchor="w")
        self.quantity_var = tk.DoubleVar(value=100)
        quantity_entry = ttk.Entry(left_frame, textvariable=self.quantity_var)
        quantity_entry.pack(fill="x", pady=5)

        # Volatility
        ttk.Label(left_frame, text="Volatility:").pack(anchor="w")
        self.volatility_var = tk.DoubleVar(value=0.05)  # default placeholder
        volatility_entry = ttk.Entry(left_frame, textvariable=self.volatility_var)
        volatility_entry.pack(fill="x", pady=5)

        # Fee Tier
        ttk.Label(left_frame, text="Fee Tier:").pack(anchor="w")
        self.fee_tier_var = tk.StringVar(value="Tier 1")
        fee_tier_dropdown = ttk.Combobox(left_frame, textvariable=self.fee_tier_var)
        fee_tier_dropdown['values'] = ["Tier 1", "Tier 2", "Tier 3"]
        fee_tier_dropdown.pack(fill="x", pady=5)

        # Submit Button
        submit_btn = ttk.Button(left_frame, text="Start Simulation", command=self.start_simulation)
        submit_btn.pack(pady=20)

        # Right Panel - Outputs
        right_frame = ttk.Frame(self, padding=10)
        right_frame.pack(side="right", fill="both", expand=True)

        ttk.Label(right_frame, text="Output Parameters", font=("Helvetica", 16)).pack(pady=10)

        self.output_text = tk.Text(right_frame, state="disabled", width=50, height=25)
        self.output_text.pack(fill="both", expand=True)

    def start_simulation(self):
        # Placeholder: clear output and show current parameters
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        params = (
            f"Exchange: {self.exchange_var.get()}\n"
            f"Spot Asset: {self.asset_var.get()}\n"
            f"Order Type: {self.order_type_var.get()}\n"
            f"Quantity: {self.quantity_var.get()}\n"
            f"Volatility: {self.volatility_var.get()}\n"
            f"Fee Tier: {self.fee_tier_var.get()}\n\n"
            "Simulation started...\n"
        )
        self.output_text.insert(tk.END, params)
        self.output_text.configure(state="disabled")

    def update_output(self, text):
        self.output_text.configure(state="normal")
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)
        self.output_text.configure(state="disabled")

if __name__ == "__main__":
    app = TradeSimulatorUI()
    app.mainloop()
