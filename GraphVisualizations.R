
#Task 3
happydata$Region <- factor(happydata$Region)
plot(happydata$Region,main = "Number of Countries in Each Region", xlab = "Region", ylab = "Count" ) 

#Task 4
#There is a very slight positive correlation between row ID and the Happiness Score. 
plot(1:nrow(happydata), happydata$`Happiness Score`,
     main = "Scatter Plot: Happiness Score vs Row ID",
     xlab = "Row ID", ylab = "Happiness Score")


#Task 5
# I learned that Africa seems to have the most variation when it comes to the happiness score. Pan America seems to have the least variation, however it has the highest median at around 6. 
plot(happydata$Region, happydata$`Happiness Score`, 
     main = "Boxplot of Happiness Score by Region", 
     xlab = "Region", ylab = "Happiness Score")
library(ggpubr)


#Task 6
#
ggboxplot(data = happydata, x = "Region", y = "Happiness Score",
          title = "Boxplot of Happiness Score by Region",
          xlab = "Region", ylab = "Happiness Score")

#Task 7
#I learned that the median for happiness scores lies around 5 and 6. The distribution seems to 
#be relatively normally distributed.
hist(happydata$`Happiness Score`, 
     main = "Histogram of Happiness Scores",
     xlab = "Happiness Score",
     ylab = "Frequency")

#Task 8 
#I learned that the health scores tend to be strongly skewed to the left with a median falling around .8. 
hist(happydata$`Health`, 
     main = "Histogram of Health Scores",
     xlab = "Health Score",
     ylab = "Frequency")

#Task 9
#I learned that the relationship between happiness scores and health scores tends to be positively correlated. As the health score increases, so does the happiness score. 
plot(happydata$`Happiness Score`, happydata$`Health`,
     main = "Scatter Plot: Happiness Score vs Health Score",
     xlab = "Happiness Score", ylab = "Health Score")
