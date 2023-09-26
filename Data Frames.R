#Task Number 1
v1 <-1:10
print (v1)
typeof(v1)

v2 <-as.integer(v1)
print(v2)
typeof(v2)
#Task Number 2
v3 <- 10 +8 * (0:99)
print(v3)

#Task Number 3
repwords <- c("hi", "hello", "bye", "goodbye", "hey", "hii")

vlength <-50

repwordvector <-rep(repwords, length.out = vlength)
print(repwordvector)

#Task Number 4
m1 <- matrix(1:20, nrow =5, ncol=4)
print(m1)
typeof(m1)

df <- as.data.frame(m1)
print(df)
typeof(df)

#Task Number 5
df <-data.frame(col1 = rep(1:4, length.out = 20), col2 = rnorm(20), col3 = runif(20))
print (df)

df$col1 <- factor(df$col1)
print df
levels(df$col1)<- c("factor1", "factor2". "factor3", "factor4")
print(df) 

#Task Number 6 
write.table(df, file = "export.txt", sep = "\t", row.names= FALSE)
importeddf <=read.table("export.txt", header = TRUE, sep ="\t")
print(importeddf) 

#Task Number 7
write.csv(df, file = "export.csv",row.names= FALSE)
importeddf <=read.csv("export.csv")
print(importeddf) 
