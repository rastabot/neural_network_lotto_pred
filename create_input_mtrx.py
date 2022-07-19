import pandas as pd
import numpy as np
from pandas import Series
import random


def lotto():
    
    '''
    creates a row of lottery numbers
    
    '''
    
    extra=random.randint(1,7);
    numbs=[];
    numbs.append(random.randint(1,37));
    i=1
    numb=random.randint(1,37);
    while i<6 :
        if numb not in numbs:
            numbs.append(numb);
            i+=1;
        else :
            numb=random.randint(1,37);            
       
    numbs.sort();
    return numbs, extra

#-----------------------------------------------------

def fill_input_matrix(df):
    '''
    function builds a data frame of random lottery lines
    '''
    nums = Series(np.array(lotto()[0]).reshape(-1,)) # initialize an array
    extra = Series(np.array(lotto()[1]).reshape(-1,))
    row =  Series(np.concatenate((nums,extra),axis=0))
    nums_df = pd.concat([row], axis=1)       # initialize a  data frame
    for i in range(df.shape[0]-1):
        nums2 = Series(np.array(lotto()[0]).reshape(-1,))
        extra2 = Series(np.array(lotto()[1]).reshape(-1,))
        row2 =  Series(np.concatenate((nums2,extra2),axis=0))
        nums_df = pd.concat([nums_df,row2], axis=1)
    
    return nums_df.T 



