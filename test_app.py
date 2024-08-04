import unittest
import yfinance as yf
from main import get_stock_price, calculate_SMA, calculate_EMA, calculate_RSI, calculate_MACD

class TestStockFunctions(unittest.TestCase):

    def setUp(self):
        # Use a common stock ticker for testing
        self.ticker = "AAPL"
        self.window = 14

    def test_get_stock_price(self):
        price = get_stock_price(self.ticker)
        self.assertIsInstance(price, str, "The stock price should be returned as a string")
        self.assertNotEqual(price, "", "The stock price should not be an empty string")

    def test_calculate_SMA(self):
        sma = calculate_SMA(self.ticker, self.window)
        self.assertIsInstance(sma, str, "The SMA should be returned as a string")
        self.assertNotEqual(sma, "", "The SMA should not be an empty string")

    def test_calculate_EMA(self):
        ema = calculate_EMA(self.ticker, self.window)
        self.assertIsInstance(ema, str, "The EMA should be returned as a string")
        self.assertNotEqual(ema, "", "The EMA should not be an empty string")

    def test_calculate_RSI(self):
        rsi = calculate_RSI(self.ticker)
        self.assertIsInstance(rsi, str, "The RSI should be returned as a string")
        self.assertNotEqual(rsi, "", "The RSI should not be an empty string")

    def test_calculate_MACD(self):
        macd_values = calculate_MACD(self.ticker).split(", ")
        self.assertEqual(len(macd_values), 3, "MACD should return three values")
        for value in macd_values:
            self.assertIsInstance(value, str, "Each MACD component should be a string")
            self.assertNotEqual(value, "", "Each MACD component should not be an empty string")

if __name__ == '__main__':
    unittest.main()

