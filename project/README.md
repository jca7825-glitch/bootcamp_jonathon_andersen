# ETF Dilemma
**Stage:**
The problem I'd like to analyze is whether or not ETFs are actually out performing the market consistently, and at that which one's do the worst and which ones actively perfrom the best.  
## Problem Statement
In the current stage of the market we have seen many losers and many winners, so the ideal is to always pick the winners and never those that lose. Hence the want for ore experienced individuals like asset and portfolio managers to make better decisions than the non-market savvy consumer.

Taking a look at the market we can see countless options for ETFs, Mutual Funds and so-on. The list is cumbersome and unnecessary, but which one is the best? As well would it just be smarter to invest in the the S&P 500 rather than a more actively managed fund?
## Stakeholder & User
The decider is the consumer, as it is our money we need to be best informed of the likely outcomes and historical consistencies. Other stakeholders would be the risk analysts or anyone working within the company that has a motivation in the ETF success, i.e. CEOs, VPs,..etc The user is the buyer of the ETF or the customer on the secondary market.
## Useful Answer & Decision

As we can see historically the investment into the market out performs both bond market and traditional savings. Using Market statistics both in recent years and long term will allow us to see what are the best investments for the short-term and what is best for the long-term. 

We must also look at the outlier years to better understand what might to best for the most risk averse investors as well, this can be tracked by associating each week with the associated risk value. 
## Assumptions & Constraints
- We are limited to what is available to the open net, so many of the above values will be insuffucuent to make a fully confident decision off of.
- The constraint of about two weeks of class has  strong damper as well, we can only collect as much data as the time allows, thus being able to include everything will not be possible.
## Known Unknowns / Risks
- Many geopolitical risks cause market fluctuations, one in the current stage being tariffs to monitor this we could use the Vix to indicate overall market volatility in the future, so we will need to make a strict basis of past data.
- As the earlier statements what defines as good performance can differ per person, so the largest risk is how to handle risk-to-reward, in this case the opinion of best performance will be consistent to highest consistent return.
## Lifecycle Mapping
Goal → Stage → Deliverable
- <analyze the short and long term averages of ETFs and the S&P 500> → Collect the data through yahoo finance or a secondary site → <Create a CSV housing all of the possible data points>
- <Have a time based analysis of the YoY returns> → Use the obtained CSV → <Return a standardized database with the short-term and long-term YoY returns of the studied ETFs>
-<Predict the next 5 year best ETF> → Using regression analysis we can have the historical data give us a depiction of what the future could look like → <Create the final CSV with the predicted 5 year returns of each ETF against the market>
- ...
## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates

## Data Storage 

The data is stored in csv files being downloaded from alpha vantage, where they are stored in the form.

Project/Data/Raw

The finalized data will be stored as csv files in the processed file.

Project/Data/Processed
