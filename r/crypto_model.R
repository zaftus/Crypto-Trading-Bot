library(forecast)

data <- read.csv("data/btc_data.csv")
ts_data <- ts(data$price, frequency=7)
fit <- auto.arima(ts_data)
forecasted <- forecast(fit, h=5)
print(forecasted)
