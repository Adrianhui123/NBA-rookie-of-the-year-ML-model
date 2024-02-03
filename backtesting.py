from numpy import diff
import pandas as pd
from sklearn.metrics import mean_absolute_error
from Main import error_metric
stats = pd.read_csv("stats.csv")
del stats["Unnamed: 0"]
del stats["Debut"]
del stats["Yrs"]
stats = stats.fillna(0)


predictors = ["Age", 'G', 'MP', 'FG', 'FGA', '3P', '3PA', 'FT',
       'FTA', 'ORB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS','FG%',
       '3P%', 'FT%', 'MP.1', 'PTS.1', 'TRB.1', 'AST.1', 'Year']

from sklearn.linear_model import Ridge

regression = Ridge(alpha=.1)

precision = []
backtesting = []
for years in range(2000, 2022):
       train = stats[stats["Year"] < years]
       test = stats[stats["Year"] == years]
       regression.fit(train[predictors], train["Share"])
       predictions = regression.predict(test[predictors])
       predictions = pd.DataFrame(predictions, columns=["predictions"], index=test.index)
       visualization = pd.concat([test[["Player", "Share"]], predictions], axis=1)  
       visualization["Rank"] = list(range(1, visualization.shape[0]+1))
       visualization["predictions rank"] = list(range(1, visualization.shape[0]+1))
       backtesting.append(visualization)  
       precision.append(error_metric(visualization))


 
    
# need some more work here