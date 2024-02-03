from random import vonmisesvariate
from numpy import diff
import pandas as pd
import csv

from sklearn.metrics import mean_absolute_error


stats = pd.read_csv("stats.csv")
del stats["Unnamed: 0"]
del stats["Debut"]
del stats["Yrs"]
stats = stats.fillna(0)


predictors = ["Age", 'G', 'MP', 'FG', 'FGA', '3P', '3PA', 'FT',
       'FTA', 'ORB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS','FG%',
       '3P%', 'FT%', 'MP.1', 'PTS.1', 'TRB.1', 'AST.1', 'Year']

training = stats[stats["Year"] < 2022]
testing = stats[stats["Year"] == 2022]
# split data into train and test

from sklearn.linear_model import Ridge

regression = Ridge(alpha=.1)
regression.fit(training[predictors], training["Share"])
predictions = regression.predict(testing[predictors])

predictions = pd.DataFrame(predictions, columns=["predictions"], index=testing.index)
visualization = pd.concat([testing[["Player", "Share"]], predictions], axis=1) 
visualization = visualization.sort_values("Share", ascending=False)
visualization["Rank"] = list(range(1, visualization.shape[0]+1))
visualization = visualization.sort_values("predictions", ascending= False)
visualization["predictions rank"] = list(range(1, visualization.shape[0]+1))

# error metrics Give a score based on how many player is in the top 10 as we predicted
visualization = visualization.sort_values("Rank", ascending=True).head(10)

from sklearn.metrics import mean_absolute_error

def error_metric():
       # use mean absolute error to find the mean differences betweeen rank and predictions rank in the top 5
       y_true = [x for x in visualization["Rank"].head(5)]
       y_pred = [x for x in visualization["predictions rank"].head(5)]
       return mean_absolute_error(y_true, y_pred)

# >>> 3.4 in our case of 2022 rookies, and we want this as low as possible


print(visualization)

# backtesting with year before 2022

        




              
