# neural_network_lotto_pred
A personal project with the goal of predicting lottery numbers. A pointless exercise but good practice of ensemble methods

<div>
 Lottery numbers predictor
 <ol>
<li> Manually download the csv with all past raffles to get an up to date CSV from :
 https://www.pais.co.il/lotto/archive.aspx#</li>
<li> main.py:  cleans the csv, gives propper names to columns, takes only the current lottery fromat, applies Descision Trees, Random Forest and Neural Network models
<li> create_input_matrix: creates a csv or data frame of randomly generated lottery numbers</li>
<li> Because each column has a slight tendency toward certain numbers</li>
   the prediction model will be build using each column from each csv
   example : X = random_numbers_csv [1],  
             y= actual_raffle_csv[1],
             input_num[1] = lattest_raffle[1]
             model.fit(X,y)
             model.predict(input_num)</li>
<li> Outputs the numbers and the probability according to each model</li>
<li> Creates a Visualization of the numbers distribution</li>
  
 </ol>
 </div>
