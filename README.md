# neural_network_lotto_pred
A personal project with the goal of predicting lottery numbers. A pointless exercise but good practice of ensemble methods

<div>Lottery numbers predictor
1. Manually download the csv with all past raffles to get an up to date CSV from :
 https://www.pais.co.il/lotto/archive.aspx#
2. main.py:  cleans the csv, gives propper names to columns, takes only the current lottery fromat, applies Descision Trees, Random Forest and Neural Network models
3. create_input_matrix: creates a csv or data frame of randomly generated lottery numbers
4. Because each column has a slight tendency toward certain numbers
   the prediction model will be build using each column from each csv
   example : X = random_numbers_csv [1],  
             y= actual_raffle_csv[1],
             input_num[1] = lattest_raffle[1]
             model.fit(X,y)
             model.predict(input_num)
5. Outputs the numbers and the probability according to each model
6. Creates a Visualization of the numbers distribution
             
            </div>
