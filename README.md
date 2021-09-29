# Bank Forex Tool

Webscraping data from the [Fubon Bank USD forex website](https://www.fubon.com/banking/personal/deposit/exchange_rate/exchange_rate_tw_photo.htm?urlParameter=1D&currency=USD)

Using Python, Autoregressive Model to finish this project

---
1. Customization tools
* You can check the exchange rate of the day
* Enter the lowest price you are currently willing to buy to confirm if you can buy
* Enter the highest price you are willing to sell at to check if you can sell

![](https://i.imgur.com/o9qhxJt.png)

---
2. Predict the selling and buying price
This data is the trend of the U.S. dollar within six months

![](https://i.imgur.com/PXmcYBS.png)
![](https://i.imgur.com/JYMzQnc.png)

Use Autoregressive Model to predict the following price
```
model = AutoReg(data, lags=1)
model_fit = model.fit()
yhat = model_fit.predict(len(data), len(data))
print(yhat)
```
