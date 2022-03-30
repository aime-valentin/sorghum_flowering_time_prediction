
class FloweringEnsembleModel(FloweringModel):

    def __init__(self, model, pca = False, n_components = None) #TODO: define argument types
        self.pca = pca
        self.model = model
        self.n_components = n_components

    def fit(self, xtrain, ytrain):
        pass

    def predict(self, xtest):
        pass

    def evaluate(self):
        pass

    def optimize(self, method = 'grid_cv'):
        pass
        
