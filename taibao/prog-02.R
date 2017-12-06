########################################################
# Description:
# 1.for threshold regression simulation
# 2.No.: 02
# 3.Purpose: threshold quantile regression
# 4.Reference: non
# 5.Author: Qifa Xu
# 6.Founded: Mar 17, 2015.
# 7.Revised: Mar 18, 2015.
########################################################
# Contents:
# 1. read data
# 2. data process
# 3. make model in mean regression
# 4. make model in quantile regression
# 5. make threshold model in mean regression
# 6. make threshold model in quantile regression
#########################################################

# 0. initialize
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
dat <- na.omit(dat)

plot(dat$sale~dat$price)

round(cor(dat), digits=4)

# 3. make model in mean regression
model.lm <- lm(sale~., data=dat)
summary(model.lm)

# 4. make model in quantile regression
library(quantreg)
taus <- seq(0.1, 0.9, length=5)
model.rq <- rq(sale~., tau=taus, data=dat)
plot(summary(model.rq))
summary(model.rq)
round(coef(model.rq), digits=4)

# 5. make threshold model in mean regression
# (1) define functions
source('sub-02.R')

# (2) find the optimal threshold
(gamopt <- gamsearch.mr(var=price, dat=dat))

# (3) estimate threshold model
thrmodel.mr <- lm(sale~price+I(price*(price>gamopt))+grade+credit
                  +popular+RevAmou+RevGrad+No, data=dat)
summary(thrmodel.mr)

# (1) make model
(thrmodel.mr <- lm(y~x1+I(x1*(x1>gamopt)), data=dat))
summary(thrmodel.mr)

# (2) show results
prices <- seq(min(dat$price), max(dat$price), length=6838)
sales.hat <- predict(thrmodel.mr, newdata=data.frame(price=prices))

plot(dat$x1, y, xlab='x', ylab='y')
lines(xs[xs<gamopt], ys.hat[xs<gamopt], lwd=2, col='blue')
lines(xs[xs>=gamopt], ys.hat[xs>=gamopt], lwd=2, col='red')
# sale~price+I(price*(price>gamma))+grade+credit+popular+RevAmou+RevGrad+No

# 6. make threshold model in quantile regression
# (1) define functions


# (2) find the optimal threshold
tau <- 0.1
(gamopt.qr <- gamsearch.qr(dat=dat, tau=tau, var=price))


# (3) estimate threshold model
thrmodel.qr <- rq(sale~price+I(price*(price>gamopt.qr))+grade+credit
                  +popular+RevAmou+RevGrad+No, tau=tau, data=dat)
summary(thrmodel.qr)
# 5. estimate threshold regression model
# (1) make model
(thrmodel.qr.1 <- rq(sale~price+I(price*(price>gamopt)), tau=taus[1], data=dat))
(thrmodel.qr.2 <- rq(sale~price+I(price*(price>gamopt)), tau=taus[2], data=dat))
(thrmodel.qr.3 <- rq(sale~price+I(price*(price>gamopt)), tau=taus[3], data=dat))
(thrmodel.qr.4 <- rq(sale~price+I(price*(price>gamopt)), tau=taus[4], data=dat))
(thrmodel.qr.5 <- rq(sale~price+I(price*(price>gamopt)), tau=taus[5], data=dat))
summary(thrmodel.qr)
coef(thrmodel.qr)   # compare with those true values
# eps <- rchisq(n=n, df=3)
# y <- beta[1] + beta[2]*x[,1] + beta[3]*(x[,1]*(x[,1] > threshold)) + x[,1]*eps
# Q.y <- beta[1] + beta[2]*x[,1] + beta[3]*(x[,1]*(x[,1] > threshold)) + x[,1]*F.inv(eps)
(F.inv <-qchisq(p=taus, df=3))
beta[2] + F.inv     # slopes in the lower interval
beta[2] + beta[3] + F.inv     # slopes in the upper interval

# (2) show results
xs <- seq(min(dat$price), max(dat$price), length=6838)
ys.hat.1 <- predict(thrmodel.qr.1, newdata=data.frame(price=xs))
ys.hat.2 <- predict(thrmodel.qr.2, newdata=data.frame(price=xs))
ys.hat.3 <- predict(thrmodel.qr.3, newdata=data.frame(price=xs))
ys.hat.4 <- predict(thrmodel.qr.4, newdata=data.frame(price=xs))
ys.hat.5 <- predict(thrmodel.qr.5, newdata=data.frame(price=xs))
cbind(ys.hat.1,ys.hat.2,ys.hat.3,ys.hat.4,ys.hat.5)
plot(dat$price, sale, xlab='price', ylab='sale')
for (i in 1:length(taus)){
  lines(xs[xs<gamopt], ys.hat[xs<gamopt,i], lty=i, lwd=2)
  lines(xs[xs>=gamopt], ys.hat[xs>=gamopt,i], lty=i, lwd=2)
}

