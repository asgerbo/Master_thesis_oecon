install.packages("zoo")
library(zoo)
  
install.packages("caTools")
library(caTools)

install.packages("dplyr")
library(dplyr)

install.packages("ggplot2")
library(ggplot2)


#import data (macrovariables.csv)
df <- macrovariables
View(df)

#price change from prev. day
df$Price_Change <- c(NA, diff(df$usd_eur_exchange))


#first value na -> remove
df <- na.omit(df)


#summary statistics (min, max, mean and quantiles. 1st-3rd quantile is 50% of data, so could consider those as threshold)
summary(df$Price_Change)

#histogram - very normalized data
hist(df$Price_Change, breaks = 200, main = "Distribution of Price Changes")

#set thresholds here
lower_threshold <- -0.002
upper_threshold <- 0.002

#labels, 0-2 with 0 down, 1 neutral and 2 up
df$Label <- cut(df$Price_Change, 
                breaks = c(-Inf, lower_threshold, upper_threshold, Inf), 
                labels = c("0", "1", "2"))

#distribution of labels. We could make this 33/33/33  percent decisions. Or 50/25/50. Idk
table(df$Label)





#If we want to get a more informative gg plot on statistics
quantiles <- quantile(df$Price_Change, probs = c(0.25, 0.75))

mean_change <- mean(df$Price_Change)

std_change <- sd(df$Price_Change)

ggplot(data.frame(df$Price_Change), aes(x = df$Price_Change)) +
  geom_histogram(binwidth = 0.0001, fill = "blue", alpha = 0.7) +
  geom_vline(aes(xintercept = quantiles[1]), color = "red", linetype = "dashed", size = 1) +
  geom_vline(aes(xintercept = quantiles[2]), color = "red", linetype = "dashed", size = 1) +
  geom_vline(aes(xintercept = mean_change), color = "green", linetype = "dotted", size = 1) +
  ggtitle("Distribution of exchange rate changes") +
  xlab("Price Change") +
  ylab("Frequency")
