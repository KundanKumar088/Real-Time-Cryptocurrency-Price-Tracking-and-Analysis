🪙 Real-Time Cryptocurrency Price Tracker
A Python-based automation project that retrieves real-time cryptocurrency data using the CoinGecko API, analyzes the market, and identifies the top 10 gainers and top 10 losers based on 24-hour price change.

This project is designed for daily crypto monitoring, data collection, and analysis — ideal for students, traders, and developers learning about API integration and data handling in Python.
🚀 Features
•	Fetches live crypto market data from the CoinGecko API
•	Extracts key information: price, market cap, volume, highs/lows, and 24h performance
•	Identifies Top 10 Gainers and Top 10 Losers
•	Automatically adds timestamps for daily tracking
•	Saves data into CSV files for long-term analysis
•	Displays summary reports directly in the terminal
📘 Explanation of Each Feature
1. **Live Data Fetching:** The project connects to the CoinGecko API to obtain real-time cryptocurrency market data such as price, volume, and market capitalization.
2. **Data Extraction:** The script uses the `requests` library to get data from the API and then structures it into a pandas DataFrame for easier manipulation.
3. **Top 10 Identification:** The DataFrame is sorted by the 24-hour price change percentage to identify the biggest gainers and losers.
4. **Timestamp Addition:** A timestamp is added using the `datetime` module to record the exact date of data retrieval.
5. **Data Storage:** All processed data is saved into CSV files for future reference or further analysis.
6. **Terminal Output:** The top gainers and losers are printed directly in the terminal, making it easy to view daily insights.
🧰 Technologies Used
•	Python — Programming language used for data processing and automation.
•	Requests — Used to send HTTP requests to the CoinGecko API.
•	Pandas — For data manipulation, sorting, and exporting to CSV.
•	Datetime — To handle timestamps and date-based file naming.
•	CoinGecko API — Provides real-time cryptocurrency data.
🧠 How It Works
1.	Fetch Data: Sends a request to the CoinGecko API for the top 250 cryptocurrencies (by market cap).
2.	Process Data: Converts the API response into a structured DataFrame.
3.	Analyze: Identifies top 10 cryptos with the highest and lowest price changes.
4.	Save Results: Exports results into daily CSV files with a date-based filename.
5.	Display Results: Prints summaries directly in the console.
📂 Output Files
The script generates the following files:
•	crypto_all_YYYY-MM-DD.csv — Contains all 250 cryptocurrencies' data for the day.
•	top_positive_10_YYYY-MM-DD.csv — Top 10 cryptocurrencies with the highest 24-hour price increase.
•	top_negative_10_YYYY-MM-DD.csv — Top 10 cryptocurrencies with the highest 24-hour price decrease.
⚙️ Setup Instructions

6.	Navigate to the project folder: cd crypto-price-tracker
7.	Create and activate a virtual environment.
8.	Install required dependencies: pip install pandas requests
9.	Run the script: python app.py
🔮 Future Enhancements
•	Email automation to send daily reports automatically.
•	Interactive dashboards using Streamlit or Flask.
•	Database storage (MySQL or MongoDB).
•	Visual data analytics using Matplotlib or Plotly.
•	Real-time price alerts and notifications.
🧑‍💻 Author
Kundan Kumar — Minor Project (Python)
Demonstrating real-time data analysis using APIs and pandas.

