########################################################
# Description:
# 1.for threshold regression simulation
# 2.No.: 01
# 3.Purpose: threshold mean regression
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
setwd('F:/programe/paper/QR+goods')
rm(list=ls())

# 1. generate data
beta <- c(3,2,10)
threshold <- 0.3
n <- 200
x <- matrix(runif(n), nrow=n, ncol=1)
eps <- rnorm(n=n)
y <- beta[1] + beta[2]*x[,1] + beta[3]*(x[,1]*(x[,1] > threshold)) + eps
dat <- data.frame(y=y, x1=x[,1])
plot(dat$x1, y)

# 2. do regression with real data
lm(y~x1+I(x1*(x1>threshold)), data=dat)

# 3. define functions
source('sub-01.R')

# 4. find the optimal threshold
(gamopt <- gamsearch.mr(var=dat$x1, dat))

# 5. estimate threshold regression model
# (1) make model
(thrmodel.mr <- lm(y~x1+I(x1*(x1>gamopt)), data=dat))
summary(thrmodel.mr)

# (2) show results
xs <- seq(min(dat$x1), max(dat$x1), length=500)
ys.hat <- predict(thrmodel.mr, newdata=data.frame(x1=xs))

plot(dat$x1, y, xlab='x', ylab='y')
lines(xs[xs<gamopt], ys.hat[xs<gamopt], lwd=2, col='blue')
lines(xs[xs>=gamopt], ys.hat[xs>=gamopt], lwd=2, col='red')



