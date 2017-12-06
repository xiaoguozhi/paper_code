# sub functions for goods pricing
# 1. define loss function for mean regression
loss.mr <- function(gam, dat){
  fmla <- y ~ x1 + I(x1 * (x1 > gam))
  model <- lm(formula=fmla, data=dat)
  sse <- sum(model$residuals^2)
  sse
}

# 2. define gamma serch function
gamsearch.mr <- function(var=x, dat){
#   browser()
  min <- min(var)
  max <- max(var)
  gams <- seq(min, max, length=500)
  los <- rep(NA, length(gams))
  for (i in 1:length(gams)){
    los[i] <- loss.mr(gam=gams[i], dat=dat)
  }
  plot(gams, los, type='l')
  optgam <- gams[which.min(los)]
  optgam
}

# 3. define loss function for quantile regression
loss.qr <- function(gam, tau, dat){
  fmla <- y ~ x1 + I(x1 * (x1 > gam))
  model <- rq(fmla, tau=tau, data=dat)
  rho <- model$rho
  rho
}


# 4. define gamma serch function for quantile regression
gamsearch.qr <- function(var=x, tau, dat){
  min <- min(var)*1.2
  max <- max(var)/1.2
  gams <- seq(min, max, length=100)
  los <- rep(NA, length(gams))
  for (i in 1:length(gams)){
    los[i] <- loss.qr(gam=gams[i], tau=tau, dat=dat)
  }
  plot(gams, los, type='l')
  optgam <- gams[which.min(los)]
  optgam
}

