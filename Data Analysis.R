# Task 1
library(dplyr)
install.packages("tidyverse")
install.packages("ggpubr")
install.packages("rstatix")
library(tidyverse)
library(ggpubr)
library(rstatix)

#Task 2
library(readr)
#Task 3
happydata <- read_csv("Downloads/happiness-2.csv")
View(happydata)
#Task 5
mean(happydata$`Happiness Score`, na.rm = TRUE)
median(happydata$`Happiness Score`, na.rm = TRUE)

(v <- happydata$`Happiness Score`)
(uniqv <- unique(v))
(positions = match(v,uniqv))
(freq = tabulate(positions))
(maxfreq <- which.max(freq))
(uniqv[maxfreq])
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

(getmode(v))
#Task 6 

#standard deviation
sd(happydata$`Happiness Score`)

#variance
var(happydata$`Happiness Score`)

#min
min(happydata$`Happiness Score`)

#max
max(happydata$`Happiness Score`)

#range
range(happydata$`Happiness Score`)

#quantile
quantile(happydata$`Happiness Score`)

#Task 7
sapply(happydata, mean,na.rm = TRUE) # note the warning message for non-numeric variables

sapply(happydata, sd,na.rm = TRUE)

#Task 8 
summary(happydata)

#Task 9
#From the result, I learned that Pan America has the greatest mean and lowest standard deviation meaning it has the lowest variance of happiness scores. Africa has the lowest mean while Pacific Asia has the greatest standard deviation. 
happydata %>%
  group_by(Region) %>%
  get_summary_stats(`Happiness Score`, type="mean_sd")

