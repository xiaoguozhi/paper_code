

setwd('E:/QR+goods')
rm(list=ls())
# 1. read data
library(xlsx)
dat <- read.xlsx(file='IPAD.xlsx', sheetName='all', startRow=1, endRow=436, colIndex=2:9)
head(dat)
class(dat)
names(dat) <- c('credit', 'grade', 'popular', 'price', 'sale', 'RevAmou', 'RevGrad', 'No')
summary(dat)

# 2. data process
dat <- na.omit(dat)

# data <- data.frame()
# for (j in 1:ncol(dat)){
#   data[,j] <- as.data.frame(dat[,j])
# #   data <- cbind(data, as.data.frame(dat[,j]))
# }

credit <- dat$credit
grade <- dat$grade
popular <- dat$popular
price <- as.numeric(matrix(dat$price))
sale <- as.numeric(matrix(dat$sale))
RevAmou <- as.numeric(matrix(dat$RevAmou))
RevGrad <- dat$RevGrad
No <- dat$No

dat <- data.frame(sale, credit, grade, popular, price, RevAmou, RevGrad, No)

plot(dat$sale~dat$price)


cor(dat)

# 3. make model in mean regression
model.lm <- lm(sale~., data=dat)
summary(model.lm)

# 4. make model in quantile regression
library(quantreg)
taus <- seq(0.1, 0.9, length=5)
model.rq <- rq(sale~., tau=taus, data=dat)
plot(summary(model.rq))
summary(model.rq)


# 5. make threshold model in mean regression
# (1) define functions
source('sub.R')

# (2) find the optimal threshold
(gamopt <- gamsearch(dat=dat))

# (3) estimate threshold model
thrmodel.lm <- lm(sale~price+I(price*(price>gamopt))+grade+credit
                  +popular+RevAmou+RevGrad+No, data=dat)
summary(thrmodel.lm)
round(coef(thrmodel.lm), digits=4)

# 6. make threshold model in quantile regression
# (1) define functions


# (2) find the optimal threshold
tau <- 0.7
(gamopt.rq <- gamsearch.rq(dat=dat, tau=tau, var=price))


# (3) estimate threshold model
thrmodel.rq <- rq(sale~price+I(price*(price>gamopt.rq))+grade+credit
                  +popular+RevAmou+RevGrad+No, tau=tau, data=dat)
summary(thrmodel.rq)
