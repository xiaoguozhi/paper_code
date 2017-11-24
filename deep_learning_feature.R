

setwd("D:/Rdata/Third_paper/third_paper_data")

library(readxl)
library(h2o)
library(dplyr)

h2o.init(nthreads = -1)
 
rm(list = ls())

set.seed(12345)

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

dat4<-dat3[1:348,]

splits <- h2o.splitFrame(dat4, ratios = 0.8, seed = 12345)




# first part of the data, without labels for unsupervised learning
train <- splits[[1]]

# second part of the data, with labels for supervised learning
valid <- splits[[2]]

test<-dat3[349:358,]

#dim(train_supervised)











DL_pre_time_1<-Sys.time()
dl <- h2o.deeplearning(
  model_id="dl", 
  training_frame=train, 
  validation_frame=valid,   ## validation dataset: used for scoring and early stopping
  x=x,
  y=y,
  hidden = c(200,200,200),
  #hidden=c(200,200,200),       ## default: 2 hidden layers with 200 neurons each
  epochs=1000,
  variable_importances=T ,
  seed = 12345,
  l1=0.001,
  l2=0.001
  
  ## not enabled by default
)
DL_pre_time_2<-Sys.time()
DL_run_time<-(DL_pre_time_2-DL_pre_time_1)

h2o.varimp_plot(dl,num_of_features = 15)





#plot(dl)








#####random forset
## run our first predictive model
RF_pre_time_1<-Sys.time()
rf <- h2o.randomForest(         ## h2o.randomForest function
  training_frame = train,        ## the H2O frame for training
  validation_frame = valid,      ## the H2O frame for validation (not required)
  x=x,                           ## the predictor columns, by column index
  y=y,                           ## the target index (what we are predicting)
  model_id = "rf_covType_v1",    ## name the model in H2O
                                 ##   not required, but helps use Flow
  ntrees = 200,                  ## use a maximum of 200 trees to create the
                                 ##  random forest model. The default is 50.
                                 ##  I have increased it because I will let 
                                 ##  the early stopping criteria decide when
                                 ##  the random forest is sufficiently accurate
  stopping_rounds = 2,           ## Stop fitting new trees when the 2-tree
                                 ##  average is within 0.001 (default) of 
                                 ##  the prior two 2-tree averages.
                                 ##  Can be thought of as a convergence setting
  score_each_iteration = T,      ## Predict against training and validation for
                                 ##  each tree. Default will skip several.
  seed = 12345)                ## Set the random seed so that this can be

RF_pre_time_2<-Sys.time()
RF_run_time<-(RF_pre_time_2-RF_pre_time_1)


GBM_pre_time_1<-Sys.time()
gbm <- h2o.gbm(
  training_frame = train,     ##
  validation_frame = valid,   ##
  x=x,                        ##
  y=y,                        ## 
  ntrees = 200,               ## decrease the trees, mostly to allow for run time
  ##  (from 50)
  learn_rate = 0.2,
   ## increase the learning rate (from 0.1)
  max_depth = 10,             ## increase the depth (from 5)
  stopping_rounds = 2,        ## 
  stopping_tolerance = 0.01,  ##
  score_each_iteration = T,   ##
  model_id = "gbm_covType3",  ##
  seed = 12345)             ##

GBM_pre_time_2<-Sys.time()
GBM_run_time<-(GBM_pre_time_2-GBM_pre_time_1)


plot(gbm)

pre1<-h2o.predict(object = gbm,newdata = test)
pre2<-h2o.predict(object = dl,newdata = test)
pre3<-h2o.predict(object = rf,newdata = test)

pre1_d<-as.data.frame(pre1$predict)
pre2_d<-as.data.frame(pre2$predict)
pre3_d<-as.data.frame(pre3$predict)


pre1_3<-cbind(pre1_d,pre2_d,pre3_d,as.data.frame(test$E_demand))

names(pre1_3)<-c("GBM","DL","RF","E_demand")

GBM_MAE<-mean(abs(pre1_3$GBM-pre1_3$E_demand))
DL_MAE<-mean(abs(pre1_3$DL-pre1_3$E_demand))
RF_MAE<-mean(abs(pre1_3$RF-pre1_3$E_demand))

GBM_MAE
DL_MAE
RF_MAE



GBM_MAPE<-mean(abs(pre1_3$GBM-pre1_3$E_demand)/pre1_3$E_demand)
DL_MAPE<-mean(abs(pre1_3$DL-pre1_3$E_demand)/pre1_3$E_demand)
RF_MAPE<-mean(abs(pre1_3$RF-pre1_3$E_demand)/pre1_3$E_demand)

GBM_MAPE
DL_MAPE
RF_MAPE

GBM_MRPE<-max(abs(pre1_3$GBM-pre1_3$E_demand)/pre1_3$E_demand)
DL_MRPE<-max(abs(pre1_3$DL-pre1_3$E_demand)/pre1_3$E_demand)
RF_MRPE<-max(abs(pre1_3$RF-pre1_3$E_demand)/pre1_3$E_demand)

GBM_MRPE
DL_MRPE
RF_MRPE






lianyungang_var_im_dl<-as.data.frame(h2o.varimp(dl))

lianyungang_var_im_rf<-as.data.frame(h2o.varimp(rf))

lianyungang_var_im_gbm<-as.data.frame(h2o.varimp(gbm))

write.csv(lianyungang_var_im_dl,file='SZ_var_im_dl.csv')
write.csv(lianyungang_var_im_rf,file='SZ_var_im_rf.csv')
write.csv(lianyungang_var_im_gbm,file='SZ_var_im_gbm.csv')



predict_lianyungang_result<-data.frame(GBM_MAE,DL_MAE,RF_MAE,
                                       GBM_MAPE,DL_MAPE,RF_MAPE,
                                       GBM_MRPE,DL_MRPE,RF_MRPE,
                                       DL_run_time,
                                       RF_run_time,
                                       GBM_run_time)



write.csv(predict_lianyungang_result,file="predict25_lianyungang_result.csv")
write.csv(pre1_3,file="predict25_lianyungang.csv")








##################################################################



pred_all<-list()
taus<-seq(from=0.01,to=0.99,length=99)
quantile_pre_time_1<-Sys.time()
for(i in 1:10)
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

write.csv(data,file="quantile_m.csv")

data1<-as.matrix(data[11,])
d<-test$E_demand[11]
data_pdf <- akj(data1, data1)








