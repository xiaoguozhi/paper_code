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
# 1. generate data
# 2. do regression with real data
#########################################################

# 0. initialize
setwd('E:/QR+goods')
rm(list=ls())

# 1. generate data
beta <- c(3, 2, 5)
threshold <- 0.3
n <- 200
x <- matrix(runif(n), nrow=n, ncol=1)
eps <- rchisq(n=n, df=3)
y <- beta[1] + beta[2]*x[,1] + beta[3]*(x[,1]*(x[,1] > threshold)) + x[,1]*eps/10
dat <- data.frame(y=y, x1=x[,1])
plot(dat$x1, y)

# 2. do regression with real data
library(quantreg)
taus <- seq(0.1, 0.9, by=0.2)
rq(y~x1+I(x1*(x1>threshold)), tau=taus, data=dat)

# 3. define functions
source('sub-01.R')

# 4. find the optimal threshold
gamopt <- rep(NA, length=length(taus))
for (i in seq_along(taus)){
  gamopt[i] <- gamsearch.qr(var=dat$x1, tau=taus[i], dat)
}
names(gamopt) <- paste('tau=', taus, sep='')
print(gamopt)


# 5. estimate threshold regression model
# (1) make model
(thrmodel.qr <- rq(y~x1+I(x1*(x1>gamopt[1])), tau=taus, data=dat))
summary(thrmodel.qr)
coef(thrmodel.qr)      # compare with those true values
# eps <- rchisq(n=n, df=3)
# y <- beta[1] + beta[2]*x[,1] + beta[3]*(x[,1]*(x[,1] > threshold)) + x[,1]*eps
# Q.y <- beta[1] + beta[2]*x[,1] + beta[3]*(x[,1]*(x[,1] > threshold)) + x[,1]*F.inv(eps)
(F.inv <-qchisq(p=taus, df=3))
beta[2] + F.inv     # slopes in the lower interval
beta[2] + beta[3] + F.inv     # slopes in the upper interval

# (2) show results
xs <- seq(min(dat$x1), max(dat$x1), length=500)
ys.hat <- predict(thrmodel.qr, newdata=data.frame(x1=xs))

plot(dat$x1, y, xlab='x', ylab='y')
for (i in 1:length(taus)){
  lines(xs[xs<gamopt], ys.hat[xs<gamopt,i], lty=i, lwd=2)
  lines(xs[xs>=gamopt], ys.hat[xs>=gamopt,i], lty=i, lwd=2)
}



