library(ggplot2)
data <- read.csv("data/btc_data.csv")
ggplot(data, aes(x=timestamp, y=price)) + geom_line() + theme_minimal()
