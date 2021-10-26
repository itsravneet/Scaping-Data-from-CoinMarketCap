# Scaping-Data-from-CoinMarketCap

In this case, you will download data and create a table and a graph.

You must use python. If you do manual work outside python (not preferred) then you must describe the steps you took so they could be replicated by someone else.

# Step 1: Download data

Collect data from 20 assets from coinmarketcap into a single table.

The URL path is
https://coinmarketcap.com/currencies/nameofasset/markets/

Here `nameofasset` is replaced with a specific name for example bitcoin or internet-computer as such: https://coinmarketcap.com/currencies/internet-computer/

The columns collected are Source, Pairs, Price, +2% Depth, -2% Depth, Volume, Volume %, Confidence, Liquidity, Updated.

Rename Pairs to Symbol. Rename Source to Exchange (abbreviated ex below).

Fetch this data for the top 20 coins on https://coinmarketcap.com/coins/

You will thus download data from 20 different URLs and concatenate them into a single table.

It's best if you connect to the API, but if this information is not available in their API you could use a python web scraping tool to do the job.

Create the columns "Base" and "Quote" from "Symbol" so BTC/USD is base=BTC quote=USD.

# Step 2: Visualize

A "market" is defined as a combination of exchange and tradingpair e.g. BTC/USD on binance.

## Table

Create a table where you, for each tradingpair, show its five most liquid exchanges as measured by the column "Volume".

columns: symbol, ex, volume, volume%, +2% depth, -2% depth

title: volume on the selected markets yyyy-mm-dd (cmc).
But replace yyyy-mm-dd with the date you grabbed the data.

Display numbers in scientific notation in the table if possible using two decimals e.g. 1.23E6 since we want to look at size, not its precision.

## Plot

title: volume on the selected markets yyyy-mm-dd (cmc)
stacked bar chart of the previous table with the same name.
x axis: quote.
y axis: sum volume
color by: exchange
legend: name of exchange

It's fine if you only graph quotes /USD and /USDT.

Save one .png for each asset. Name the file something good.

Create one plot for each asset and put them inside a 5*4 matrix so we can see all at once.
