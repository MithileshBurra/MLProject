import os 
from src.exception import CustomException
from src.logger import logging
import dill
import sys
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    try:
        model_report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
            gs = GridSearchCV(model,para,cv = 3)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            y_pred = model.predict(X_test)
            r2score = r2_score(y_test,y_pred)
            model_report[list(models.keys())[i]] = r2score
        return model_report
    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
