from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split

clean_data(df):
    data = data_clean[['neu', 'ext', 'ope', 'agr', 'con', 'BFF_15_1', 'BFF_15_2', 'BFF_15_3', 'BFF_15_4', 'BFF_15_5', 'BFF_15_6', 'BFF_15_7', 'BFF_15_8', 'BFF_15_9', 'BFF_15_10', 'BFF_15_11', 'BFF_15_12', 'BFF_15_13', 'BFF_15_14', 'BFF_15_15']].dropna()
    return data

def predict_character(X_train,y_train,X)test,y_test):
    knn = KNeighborsRegressor(n_neighbors=20)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return y_pred


