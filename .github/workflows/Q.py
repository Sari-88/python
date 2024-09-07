import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Define Graphing Function
def make_graph(stock_data, revenue_data, stock, filename):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=.3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible=True)
    fig.write_image(f"{filename}.png")  # Save the figure as a PNG file

# Question 1: Use yfinance to Extract Stock Data
print('Question 1: Use yfinance to Extract Tesla Stock Data')
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head(5))

# For Tesla Revenue
print('Question 2: Web scraping to Extract Tesla Revenue Data')
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html5lib")
print("HTML Data Fetched")
print(soup.prettify())  # Output the HTML content to debug

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
try:
    for table in soup.find_all('table'):
        if table.find('th').getText().startswith("Tesla Quarterly Revenue"):
            for row in table.find("tbody").find_all("tr"):
                col = row.find_all("td")
                if len(col) != 2: continue
                Date = col[0].text
                Revenue = col[1].text.replace("$", "").replace(",", "")
                tesla_revenue = tesla_revenue.append({"Date": Date, "Revenue": Revenue}, ignore_index=True)
except Exception as e:
    print(f"Error while scraping Tesla revenue data: {e}")
    
tesla_revenue.dropna(subset=["Revenue"], inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail(5))  # Output the fetched data for verification


# Question 3: Extract GameStop stock data
print('Question 3: Use yfinance to Extract GME Stock Data')
gme = yf.Ticker('GME')
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head(5))

# Question 4: Web scraping GameStop revenue data
print('Question 4: Web scraping to Extract GME Revenue Data')
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html5lib")
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for table in soup.find_all('table'):
    if table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$", "").replace(",", "")
            gme_revenue = gme_revenue.append({"Date": Date, "Revenue": Revenue}, ignore_index=True)
print(gme_revenue.tail(5))

# Question 5: Plot Tesla stock graph
print('Question 5: Plot Tesla Stock Graph')
make_graph(tesla_data, tesla_revenue, 'Tesla', 'tesla_stock_graph')

# Question 6: Plot GameStop stock graph
print('Question 6: Plot GameStop Stock Graph')
make_graph(gme_data, gme_revenue, 'GameStop', 'gme_stock_graph')
