import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

class FloweringModel:

    def __init__(self, model_tpl, df_train, df_test): #TODO: define argument types
        self.model_name, self.model = model_tpl
        self.df_train = df_train
        self.df_test = df_test

    def fit(self):
        xtrain = self.df_train[self.df_train.columns[:6]].values
        ytrain = self.df_train['DaysToBloom'].values
        self.model.fit(xtrain, ytrain)

    def predict(self, xtest):
        return self.model.predict(xtest)

    def evaluate(self):
        return (self._evaluate_test(), self._evaluate_train())
    def _evaluate_test(self):
        #evaluation metrics: r2_score, MAE, and RMSE
        xtest = self.df_test[self.df_test.columns[:6]].values
        ytest = self.df_test['DaysToBloom'].values
        ypred = self.model.predict(xtest)

        r2_ = r2_score(ytest,ypred)
        mae = mean_absolute_error(ytest, ypred)
        rmse = np.sqrt(mean_squared_error(ytest,ypred))

        return pd.DataFrame.from_dict({
        "Model": [self.model_name],
        "R^2": [r2_],
        "MAE": [mae],
        "RMSE": [rmse]
        })
    def _evaluate_train(self):
        #evaluation metrics: r2_score, MAE, and RMSE
        xtrain = self.df_train[self.df_train.columns[:6]].values
        ytrain = self.df_train['DaysToBloom'].values
        ypred = self.model.predict(xtrain)

        r2_ = r2_score(ytrain,ypred)
        mae = mean_absolute_error(ytrain, ypred)
        rmse = np.sqrt(mean_squared_error(ytrain,ypred))

        return pd.DataFrame.from_dict({
        "Model": [self.model_name],
        "R^2": [r2_],
        "MAE": [mae],
        "RMSE": [rmse]
        })


    def optimize(self, method = 'grid_cv'):
        pass
