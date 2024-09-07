#Define Graphing Function

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


print ('Question 1: Use yfinance to Extract Stock Data') 

#Define the ticker 
tesla = yf.Ticker('TSLA')

tesla_data = tesla.history(period="max")
#Reset the index 

tesla_data.reset_index(inplace=True)
tesla_data.head(5)

print('Question 2: Use Webscraping to Extract Tesla Revenue Data') 

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text

#Parse the html data using beautiful_soup.

soup = BeautifulSoup(html_data, "html5lib")
#print(soup.prettify())

tesla_revenue = pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("Tesla Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$","").replace(",","")
               
            tesla_revenue = tesla_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)


tesla_revenue.dropna(axis=0, how='all', subset=['Revenue'])


tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""] 

tesla_revenue.tail(5)

print('Question 3: Use yfinance to Extract Stock Data') 

# Ticker symbol is GME.

gme = yf.Ticker('GME')

gme_data = gme.history(period = "max")
gme_data.reset_index(inplace=True)
gme_data.head(5). 

print ('Question 4: Use Webscraping to Extract GME Revenue Data') 

#define the website url to Extract data 

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text

#Parse the html data using beautiful_soup.

soup = BeautifulSoup(html_data, "html5lib")
#print(soup.prettify())

gme_revenue = pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$","").replace(",","")
               
            gme_revenue = gme_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)

#Display the last five rows of the gme_revenue using the tail function.

gme_revenue.tail(5)

print ('Question 5: Plot Tesla Stock Graph') 


make_graph(tesla_data, tesla_revenue, 'Tesla')

make_graph(tesla_data, tesla_revenue, 'Tesla')

print ('Question 6: Plot GameStop Stock Graph') 

make_graph(gme_data, gme_revenue, 'GameStop').
