from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from pandas import Series, DataFrame
import numpy as np
import pandas as pd



def model_predict(X1,y1,input_num1):
    '''
    Parameters
    ----------
    X : LIST input column vector
    y : LIST target vector
    input_num : LIST  input to predict from

    Returns
    -------
    the prediction  according to decissiont trees, random forest and neural netwokrs
    using GridsearchCV

    '''
    
    #y = df[['1']]
    
    X = (np.expand_dims(X1, axis=1))
    y = (np.expand_dims(y1, axis=1))
    input_num = (np.expand_dims(input_num1, axis=1))
              
           
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)
    #input_num = Series(np.array(input_num).reshape(-1,1))
    #---- GRIDSEARCH DESCISSION TREES model training + cross validation  
    
    
    #print('shape of X :',X.shape)
    #print('shape of y_train :', y_train.shape)
    #print('shape of x1 :', input_num.shape)
    
    tree_params = {'criterion':['gini','entropy'],
                   'max_depth':[4,5,6,7,8,9,10,11,12,15,20,30,40,50,70,90,120,150]
                   }
    dess_tree_gs = GridSearchCV(DecisionTreeClassifier(), tree_params,verbose=False, cv=5)
    dess_tree_gs.fit(X_train, y_train)
    #d_tree_gs_pred = dess_tree_gs.predict(X_test) # test PREDICTION
    dt_score =  dess_tree_gs.best_score_
    pred1 = dess_tree_gs.predict(input_num)
    
    #---- GRIDSEARCH RANDOM FOREST model training + cross validation
    
    forest_params = {
    'n_estimators': [100, 300, 600]
    }
    rand_forest_gs = GridSearchCV(RandomForestClassifier(),param_grid = forest_params , verbose=False)
    rand_forest_gs.fit(X_train, y_train)
    #rand_forest_gs_pred = rand_forest_gs.predict(X_test)
    rf_score = rand_forest_gs.best_score_
    pred2 = rand_forest_gs.predict(input_num)
    
    #---- GRIDSEARCH NEURAL NETWORK model training + cross validation
    nn_params ={
    'hidden_layer_sizes':[(50,),(100,),(150,),(200,)]
    }
    clf_NN_gs = GridSearchCV(MLPClassifier(random_state=1,max_iter=400),param_grid = nn_params , verbose=False)
    clf_NN_gs.fit(X_train, y_train)
    #clf_NN_gs_pred = clf_NN_gs.predict(X_test)
    nn_score =  clf_NN_gs.best_score_
    pred3 = clf_NN_gs.predict(input_num)
    
    #--------------------------------------------
    print('-------------------------------------------------------------')
    #print('for X = ',X,'y = ',y,'input = ',input_num)
    print('decission trees score:',f'{dt_score:0.4f}','\n',
          'random forest score:',f'{rf_score:0.4f}','\n',
          'neural network score:',f'{nn_score:0.4f}')
    
    return pred1 ,pred2, pred3

#----------------------------------------


    
    
    
    
    
    