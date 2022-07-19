# -*- coding: utf-8 -*-
"""
The futile lottery numbers predictor

1. download the csv with all past raffles
2. clean the csv, give propper name to columns, take only the current lottery fromat
3. create a csv or data frame of randomly generated lottery numbers
4. Because each column has a slight tendency toward certain numbers
   so the prediction model will be build using each column from each csv
   example : X = random_numbers_csv [1],  
             y= actual_raffle_csv[1],
             input_num[1] = lattest_raffle[1]
             model.fit(X,y)
             model.predict(input_num)
             
             
Created on Tue Jul 21 12:59:44 2020

@author: Thor 3



"""


import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from datetime import datetime,date,timedelta
from dateutil import parser
from pandas import Series, DataFrame

from import_data import get_data_frame

from create_input_mtrx import fill_input_matrix

from build_models import model_predict


# run this once, 
# it downloads the file to the download folder
#get_data_frame()


#with open("C:\\Users\\Thor 3\\Downloads\\Lotto.csv", "r") as f:
   # file_content = f.read()
#f.close()

lotto_df =  pd.read_csv('Lotto.csv',encoding='latin-1')


cols = lotto_df.columns
new_name = {"äâøìä": "Agrala",
            "úàøéê": "Date",
            "äîñôø äçæ÷/ðåñó":'extra',
            "îñôø_æåëéí_ìåèå": 'Regular',
            "îñôø_æåëéí_ãàáì_ìåèå": 'Double'
          }

lotto_df = lotto_df.rename(columns=new_name)

lotto_df.drop('Unnamed: 11',axis=1,inplace=True)


#----- grab the last agrala

last_agrala = lotto_df.loc[0]
lotto_df = lotto_df.loc[1:943]
#---------------------------------

#lotto_df['extra'] =  lotto_df['extra'].apply(lambda x : x<8)

#print(lotto_df.head())

def parce_dates(date):
    d = date
    d = parser.parse(d)
    return d.strftime('%d/%m/%y')

lotto_df['Date'] = lotto_df['Date'].apply(parce_dates,1)

lotto_df = lotto_df.loc[:943]

# input df -------------------------
input_df = fill_input_matrix(lotto_df)

col_names={0:'1',
           1:'2',
           2:'3',
           3:'4',
           4:'5',
           5:'6',
           6:'extra'}
input_df = input_df.rename(columns=col_names)

print('-------------------------------')
print('input df shape:',input_df.shape)
print('input_df columns:',input_df.columns)
print('last_agrala:', last_agrala)

print('-------------------------------',end='\n')

#=== building the model for each column and prediction a number
X = [input_df['1'],input_df['2'],
     input_df['3'],input_df['4'],
     input_df['5'],input_df['6'],input_df['extra']]

y= [lotto_df['1'],lotto_df['2'],
     lotto_df['3'],lotto_df['4'],
     lotto_df['5'],lotto_df['6'],lotto_df['extra']]

input_x = pd.DataFrame(last_agrala)


columns =['1','2','3','4','5','6','extra']

#print(len(columns))
#print('============= >>  input_x[1]:', input_x.loc['1'])


dt_ = []
rf_ = []
nn_ =[]
x = []

print("Wait 3 minutes to get the predicted lottery numbers..")
for i in range(0,7):
    #print('i = ',i)
    #print('IN LOOP *** ==> columns[i]] = ',columns[i],'\n',
     #     'type :',type(columns[i]),'\n')
    
    x1 = np.array(input_x.loc[columns[i]])
       
     
    dt_prediction, rf_pred, nn_pred = model_predict(input_df[columns[i]],
                                                    lotto_df[columns[i]],
                                                    x1)
    dt_.append(dt_prediction)
    rf_.append(rf_pred)
    nn_.append(nn_pred)
    

last_agrala.drop(['Agrala','Date','Regular','Double',],inplace=True)  
    
df_pred =  pd.DataFrame(zip(last_agrala,dt_,rf_,nn_))
df_pred.rename(columns=({0:'input',
                        1:'dt',
                        2:'rf',
                        3:'NN'}),inplace=True)

print(df_pred)


    
    


#---------------------------------------------

def print_graphs(df,fig_name):
        
    fig, axs = plt.subplots(2,3, figsize=(16,8))    
        
    sb.countplot(x='1',data=df,ax=axs[0][0])
    sb.countplot(x='2',data=df,ax=axs[0][1])
    sb.countplot(x='3',data=df,ax=axs[0][2])
    sb.countplot(x='4',data=df,ax=axs[1][0])
    sb.countplot(x='5',data=df,ax=axs[1][1])
    sb.countplot(x='6',data=df,ax=axs[1][2])
    sb.catplot('extra',kind="count",data=df,legend=True)
    
    fig.suptitle(fig_name, fontsize=14)
    
    fig.tight_layout()

    fig.show()
    
 #--------------  
    
    

#print(lotto_df.head())

#print(type(lotto_df.loc[3209]['Date']))

p = input('print graphs \n')
if p == 'y':
    print_graphs(lotto_df,'Actual Numbers')
    print_graphs(input_df,'Generated Numbers')
    #lotto_df.info()
    print('Showing Graphs')
else:
   #lotto_df.info()
    #print(lotto_df.tail())
    print('Done')
    
    

