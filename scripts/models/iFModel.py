
from abc import ABC, abstractmethod

class FloweringModel(ABC):

    @abstractmethod
    def fit(self,xtrain, ytrain):
        pass
    @abstractmethod
    def predict(self,xtest):
        pass
    @abstractmethod
    def evaluate(self):
        pass
    @abstractmethod
    def optimize(self, method = 'grid_cv'):
        pass
