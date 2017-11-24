

rm(list = ls())
setwd("D:/Rdata/Third_paper/third_paper_data")

library(readxl)
library(h2o)
library(dplyr)

h2o.init(nthreads = -1)

set.seed(12345)

dat<-read_excel("lianyungang_total_feature.xlsx")

dim(dat)


dat1<-na.omit(dat)

dat2<-dat1[,2:58]

names(dat2)

month<-as.factor(dat1$month)

day_of_w<-as.factor(dat1$day_of_w)

air<-as.factor(dat1$air)

rain<-as.factor(dat1$rain)


levels(air)[levels(air)=="优"]<-"6"
levels(air)[levels(air)=="良"]<-"5"
levels(air)[levels(air)=="轻度污染"]<-"4"
levels(air)[levels(air)=="中度污染"]<-"3"
levels(air)[levels(air)=="重度污染"]<-"2"
levels(air)[levels(air)=="严重污染"]<-"1"

air<-as.numeric(air)

levels(month)[levels(month)=="January"]<-"1"
levels(month)[levels(month)=="February"]<-"2"
levels(month)[levels(month)=="March"]<-"3"

levels(month)[levels(month)=="April"]<-"4"
levels(month)[levels(month)=="May"]<-"5"

levels(month)[levels(month)=="June"]<-"6"
levels(month)[levels(month)=="July"]<-"7"
levels(month)[levels(month)=="August"]<-"8"
levels(month)[levels(month)=="September"]<-"9"
levels(month)[levels(month)=="October"]<-"10"
levels(month)[levels(month)=="November"]<-"11"
levels(month)[levels(month)=="December"]<-"12"

levels(month)

levels(day_of_w)[levels(day_of_w)=="Monday"]<-"1"
levels(day_of_w)[levels(day_of_w)=="Tuesday"]<-"2"
levels(day_of_w)[levels(day_of_w)=="Wednesday"]<-"3"
levels(day_of_w)[levels(day_of_w)=="Thursday"]<-"4"
levels(day_of_w)[levels(day_of_w)=="Friday"]<-"5"
levels(day_of_w)[levels(day_of_w)=="Saturday"]<-"6"
levels(day_of_w)[levels(day_of_w)=="Sunday"]<-"7"

levels(day_of_w)

dat2$month<-month
dat2$air<-air
dat2$rain<-rain
dat2$day_of_w<-day_of_w




y <- "E_demand"  #response column: digits 0-9
x <- setdiff(names(dat2), y)  #vector of predictor column names

dat3<-as.h2o(dat2,destination_frame = "dat3")

dat4<-dat3[1:333,]

splits <- h2o.splitFrame(dat4, ratios = 0.8, seed = 12345)




# first part of the data, without labels for unsupervised learning
train <- splits[[1]]

# second part of the data, with labels for supervised learning
valid <- splits[[2]]

test<-dat3[334:358,]













pred_all<-list()
taus<-seq(from=0.01,to=0.99,length=99)
quantile_pre_time_1<-Sys.time()
for(i in 1:99)
{
  m1 <- h2o.deeplearning(
    model_id="dl_model_first", 
    training_frame=train, 
    validation_frame=valid,   ## validation dataset: used for scoring and early stopping
    x=x,
    y=y,
    #activation="Rectifier",  ## default
    hidden=c(200,200,200),       ## default: 2 hidden layers with 200 neurons each
    epochs=500,
    variable_importances=T ,
    distribution = 'quantile',
    quantile_alpha = taus[i],
    seed = 12345
    ## not enabled by default
  )
  pred <- h2o.predict(m1, newdata = test)
  pred <-as.data.frame(pred$predict)
  names(pred)<-paste("quantile",taus,sep = "_")[i]
  pred_all[[i]]<-pred
}
quantile_pre_time_2<-Sys.time()

quantile_run_time_2<-(quantile_pre_time_2-quantile_pre_time_1)




data<-as.data.frame(pred_all)

write.csv(data,file="lianyungang_quantile_25m.csv")

rm(list = ls())


dat<-read_excel("suzhou_total_feature.xlsx")

dim(dat)

#dat<-h2o.importFile(path = "total_feature.xlsx",destination_frame = "dat")
#dat1<-as.data.frame(dat)
dat1<-na.omit(dat)

dat2<-dat1[,2:58]

names(dat2)

month<-as.factor(dat1$month)

day_of_w<-as.factor(dat1$day_of_w)

air<-as.factor(dat1$air)

rain<-as.factor(dat1$rain)


levels(air)[levels(air)=="优"]<-"6"
levels(air)[levels(air)=="良"]<-"5"
levels(air)[levels(air)=="轻度污染"]<-"4"
levels(air)[levels(air)=="中度污染"]<-"3"
levels(air)[levels(air)=="重度污染"]<-"2"
levels(air)[levels(air)=="严重污染"]<-"1"

air<-as.numeric(air)

levels(month)[levels(month)=="January"]<-"1"
levels(month)[levels(month)=="February"]<-"2"
levels(month)[levels(month)=="March"]<-"3"

levels(month)[levels(month)=="April"]<-"4"
levels(month)[levels(month)=="May"]<-"5"

levels(month)[levels(month)=="June"]<-"6"
levels(month)[levels(month)=="July"]<-"7"
levels(month)[levels(month)=="August"]<-"8"
levels(month)[levels(month)=="September"]<-"9"
levels(month)[levels(month)=="October"]<-"10"
levels(month)[levels(month)=="November"]<-"11"
levels(month)[levels(month)=="December"]<-"12"

levels(month)

levels(day_of_w)[levels(day_of_w)=="Monday"]<-"1"
levels(day_of_w)[levels(day_of_w)=="Tuesday"]<-"2"
levels(day_of_w)[levels(day_of_w)=="Wednesday"]<-"3"
levels(day_of_w)[levels(day_of_w)=="Thursday"]<-"4"
levels(day_of_w)[levels(day_of_w)=="Friday"]<-"5"
levels(day_of_w)[levels(day_of_w)=="Saturday"]<-"6"
levels(day_of_w)[levels(day_of_w)=="Sunday"]<-"7"

levels(day_of_w)

dat2$month<-month
dat2$air<-air
dat2$rain<-rain
dat2$day_of_w<-day_of_w




y <- "E_demand"  #response column: digits 0-9
x <- setdiff(names(dat2), y)  #vector of predictor column names

dat3<-as.h2o(dat2,destination_frame = "dat3")

dat4<-dat3[1:333,]

splits <- h2o.splitFrame(dat4, ratios = 0.8, seed = 12345)




# first part of the data, without labels for unsupervised learning
train <- splits[[1]]

# second part of the data, with labels for supervised learning
valid <- splits[[2]]

test<-dat3[334:358,]













pred_all<-list()
taus<-seq(from=0.01,to=0.99,length=99)
quantile_pre_time_1<-Sys.time()
for(i in 1:99)
{
  m1 <- h2o.deeplearning(
    model_id="dl_model_first", 
    training_frame=train, 
    validation_frame=valid,   ## validation dataset: used for scoring and early stopping
    x=x,
    y=y,
    #activation="Rectifier",  ## default
    hidden=c(200,200,200),       ## default: 2 hidden layers with 200 neurons each
    epochs=500,
    variable_importances=T ,
    distribution = 'quantile',
    quantile_alpha = taus[i],
    seed = 12345
    ## not enabled by default
  )
  pred <- h2o.predict(m1, newdata = test)
  pred <-as.data.frame(pred$predict)
  names(pred)<-paste("quantile",taus,sep = "_")[i]
  pred_all[[i]]<-pred
}
quantile_pre_time_2<-Sys.time()

quantile_run_time_2<-(quantile_pre_time_2-quantile_pre_time_1)




data<-as.data.frame(pred_all)

write.csv(data,file="suzhou_quantile_25m.csv")

rm(list = ls())



dat<-read_excel("nanjing_total_feature.xlsx")

dim(dat)

#dat<-h2o.importFile(path = "total_feature.xlsx",destination_frame = "dat")
#dat1<-as.data.frame(dat)
dat1<-na.omit(dat)

dat2<-dat1[,2:58]

names(dat2)

month<-as.factor(dat1$month)

day_of_w<-as.factor(dat1$day_of_w)

air<-as.factor(dat1$air)

rain<-as.factor(dat1$rain)


levels(air)[levels(air)=="优"]<-"6"
levels(air)[levels(air)=="良"]<-"5"
levels(air)[levels(air)=="轻度污染"]<-"4"
levels(air)[levels(air)=="中度污染"]<-"3"
levels(air)[levels(air)=="重度污染"]<-"2"
levels(air)[levels(air)=="严重污染"]<-"1"

air<-as.numeric(air)

levels(month)[levels(month)=="January"]<-"1"
levels(month)[levels(month)=="February"]<-"2"
levels(month)[levels(month)=="March"]<-"3"

levels(month)[levels(month)=="April"]<-"4"
levels(month)[levels(month)=="May"]<-"5"

levels(month)[levels(month)=="June"]<-"6"
levels(month)[levels(month)=="July"]<-"7"
levels(month)[levels(month)=="August"]<-"8"
levels(month)[levels(month)=="September"]<-"9"
levels(month)[levels(month)=="October"]<-"10"
levels(month)[levels(month)=="November"]<-"11"
levels(month)[levels(month)=="December"]<-"12"

levels(month)

levels(day_of_w)[levels(day_of_w)=="Monday"]<-"1"
levels(day_of_w)[levels(day_of_w)=="Tuesday"]<-"2"
levels(day_of_w)[levels(day_of_w)=="Wednesday"]<-"3"
levels(day_of_w)[levels(day_of_w)=="Thursday"]<-"4"
levels(day_of_w)[levels(day_of_w)=="Friday"]<-"5"
levels(day_of_w)[levels(day_of_w)=="Saturday"]<-"6"
levels(day_of_w)[levels(day_of_w)=="Sunday"]<-"7"

levels(day_of_w)

dat2$month<-month
dat2$air<-air
dat2$rain<-rain
dat2$day_of_w<-day_of_w




y <- "E_demand"  #response column: digits 0-9
x <- setdiff(names(dat2), y)  #vector of predictor column names

dat3<-as.h2o(dat2,destination_frame = "dat3")

dat4<-dat3[1:333,]

splits <- h2o.splitFrame(dat4, ratios = 0.8, seed = 12345)




# first part of the data, without labels for unsupervised learning
train <- splits[[1]]

# second part of the data, with labels for supervised learning
valid <- splits[[2]]

test<-dat3[334:358,]













pred_all<-list()
taus<-seq(from=0.01,to=0.99,length=99)
quantile_pre_time_1<-Sys.time()
for(i in 1:99)
{
  m1 <- h2o.deeplearning(
    model_id="dl_model_first", 
    training_frame=train, 
    validation_frame=valid,   ## validation dataset: used for scoring and early stopping
    x=x,
    y=y,
    #activation="Rectifier",  ## default
    hidden=c(200,200,200),       ## default: 2 hidden layers with 200 neurons each
    epochs=500,
    variable_importances=T ,
    distribution = 'quantile',
    quantile_alpha = taus[i],
    seed = 12345
    ## not enabled by default
  )
  pred <- h2o.predict(m1, newdata = test)
  pred <-as.data.frame(pred$predict)
  names(pred)<-paste("quantile",taus,sep = "_")[i]
  pred_all[[i]]<-pred
}
quantile_pre_time_2<-Sys.time()

quantile_run_time_2<-(quantile_pre_time_2-quantile_pre_time_1)



data<-as.data.frame(pred_all)

write.csv(data,file="nanjing_quantile_25m.csv")
