import heapq
import pandas as pd

class OrderBook:
    def __init__(self):
        self.bids = []  # Max-heap for buy orders
        self.asks = []  # Min-heap for sell orders

    def place_order(self, price, size, order_type):
        if order_type == "buy":
            heapq.heappush(self.bids, (-price, size))  # Max-heap (negate price for sorting)
        elif order_type == "sell":
            heapq.heappush(self.asks, (price, size))   # Min-heap (sorted in ascending order)

    def get_best_bid(self):
        return -self.bids[0][0] if self.bids else None

    def get_best_ask(self):
        return self.asks[0][0] if self.asks else None

    def match_orders(self):
        """ Match buy and sell orders when possible """
        while self.bids and self.asks and -self.bids[0][0] >= self.asks[0][0]:
            best_bid = heapq.heappop(self.bids)  # Highest bid
            best_ask = heapq.heappop(self.asks)  # Lowest ask

            trade_size = min(best_bid[1], best_ask[1])
            print(f"✅ Trade Executed: {trade_size} shares at ${best_ask[0]}")

            # If there's remaining size, push back to order book
            if best_bid[1] > trade_size:
                heapq.heappush(self.bids, (best_bid[0], best_bid[1] - trade_size))
            if best_ask[1] > trade_size:
                heapq.heappush(self.asks, (best_ask[0], best_ask[1] - trade_size))

    def display(self):
        bids_df = pd.DataFrame(self.bids, columns=["Price", "Size"])
        asks_df = pd.DataFrame(self.asks, columns=["Price", "Size"])
        print("\n📉 **Bids (Buy Orders):**")
        print(bids_df.sort_values(by="Price", ascending=False))
        print("\n📈 **Asks (Sell Orders):**")
        print(asks_df.sort_values(by="Price", ascending=True))


if __name__ == "__main__":
    book = OrderBook()

    # Adding sample buy and sell orders
    book.place_order(100, 10, "buy")
    book.place_order(101, 5, "sell")
    book.place_order(99, 8, "buy")
    book.place_order(102, 2, "sell")
    book.place_order(101, 7, "buy")
    book.place_order(100, 4, "sell")

    print("\nBefore Matching Orders:")
    book.display()

    book.match_orders()

    print("\nAfter Matching Orders:")
    book.display()
