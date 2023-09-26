
library(tidyverse)
library(ggpubr)
library(rstatix)
library(datarium)



library(readr)
iris_2 <- read_csv("Downloads/iris-2.csv")
View(iris_2)

library(readr)
iristtest_2 <- read_csv("Downloads/iristtest-2.csv")
View(iristtest_2)

library(readr)
weightanova_2 <- read_csv("Downloads/weightanova-2.csv")
View(weightanova_2)

library(readr)
weightTtest_2 <- read_csv("Downloads/weightTtest-2.csv")
View(weightTtest_2)

### 1
### T Tests
### Iris T-Test
# Descriptive Statistics
iristtest_2 %>%
  group_by(Species) %>%
  get_summary_stats(Petal.Length, type="mean_sd")

# Box Plot Visualization
ggboxplot(iristtest_2, x = "Species" , y = "Petal.Length")


# Check Assumptions

# Check outliers
iristtest_2 %>%
  group_by(Species) %>%
  identify_outliers(Petal.Length)

# check normality using the Shapiro Wilk test
iristtest_2 %>%
  group_by(Species) %>%
  shapiro_test(Petal.Length)

# qq plot
ggqqplot(iristtest_2, x = "Petal.Length", facet.by = "Species")

# Check homogeneity
iristtest_2$Species <- as.factor(iristtest_2$Species)  # Convert Species to a factor variable
iristtest_2$Petal.Length <- as.numeric(iristtest_2$Petal.Length)  # Convert Petal.Length to numeric

iristtest_2 %>%
  levene_test(Petal.Length ~ Species)


# Compute t-test

IToutput <- iristtest_2 %>%
  t_test(Petal.Length ~ Species) %>%
  add_significance()
IToutput
### Statistically significant
# the p value is less than 0.05 (7.57e-30). There is significant difference in the petal
# length of the two species. 




### 4
### Paired t-test

weightTtest.long <- weightTtest_2 %>%
  gather(key = "time", value = "weight",before,after)

view(weightTtest.long)

# Get summary statistics
weightTtest.long %>%
  group_by(time) %>%
  get_summary_stats(weight, type = "mean_sd")

# visualize the data in pairs
pairedplot <- ggpaired(weightTtest.long, x = "time", y = "weight", 
                       order = c("before", "after"),
                       ylab = "Weight", xlab = "Time point")

pairedplot

# Check assumptions
# Check outliers
# calculate the difference in each pair


weightTtest_2 <- weightTtest_2 %>% mutate(differences = before-after)
head(weightTtest_2, 5)

weightTtest_2 %>% identify_outliers(differences)

weightTtest_2 %>% shapiro_test(differences) 


# Visualize 
ggqqplot(weightTtest_2, "differences")

output <- weightTtest.long %>%
  t_test(weight ~ time, paired = TRUE) %>%
  add_significance()
output
# p is less than 0.05. There is significant different
# between the scores collected at t1 and t2


### 7
### ANOVA 
view(iris_2)
iris_2 %>% sample_n_by(Species,size = 1)

# Let's get summary of some descriptive statistics to have a feeling of the data
iris_2 %>%
  group_by(Species) %>%
  get_summary_stats(Sepal.Length, type="mean_sd")
# visualization using box plot

ggboxplot(iris_2,x="Species",y="Sepal.Length")

# check the assumptions of ANOVA
# check outliers
iris_2 %>%
  group_by(Species) %>%
  identify_outliers(Sepal.Length)

model <- lm(Sepal.Length ~Species, data = iris_2)
ggqqplot(residuals(model))

shapiro_test(residuals(model))
#Non-Significant

iris_2 %>%
  levene_test(Sepal.Length ~ Species)

pg.aov <- iris_2 %>% anova_test(Sepal.Length ~ Species)
pg.aov

# the p value (2.86e-91) is lower than 0.05. There is significant difference
# between the two species.

pg.pwc <- iris_2 %>% tukey_hsd(Sepal.Length ~ Species)
pg.pwc





### 10
### Repeated Measures ANOVA
view(weightanova_2)

weightanova_2 <- weightanova_2 %>%
  gather(key = "time", value = "weight", t1, t2, t3) %>%
  convert_as_factor(id, time) # convert id and time into factor

view(weightanova_2)

# get descriptive statistics
weightanova_2 %>%
  group_by(time) %>%
  get_summary_stats(weight, type = "mean_sd")

# box plot to understand data
bxp <- ggboxplot(weightanova_2, x = "time", y = "weight", add = "point") 
bxp

# checking assumptions
## outliers
weightanova_2 %>%
  group_by(time) %>%
  identify_outliers(weight)

## normal distribution assumption
weightanova_2 %>%
  group_by(time) %>%
  shapiro_test(weight)

ggqqplot(weightanova_2, "weight", facet.by = "time")

# computing the Repeated measures ANOVA F
res.aov <- anova_test(data = weightanova_2, dv = weight, within = time, wid = id)
get_anova_table(res.aov)


# the p value (1.84e-25) is lower than 0.05. There is significant difference 
# in the weight of mice before and after. 

# post-hoc test, use the bonferroni test
bonf <- pairwise_t_test(data = weightanova_2, 
                        weight~time,
                        paired = T,
                        p.adjust.method = "bonferroni")
bonf
