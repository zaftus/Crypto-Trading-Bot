data <- read.csv("data/btc_data.csv")
data$return <- c(0, diff(log(data$price)))
cumulative_return <- cumsum(data$return)
plot(cumulative_return, type='l', main='Backtest BTC')
