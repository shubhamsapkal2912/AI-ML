'''#25. Perform pre-processing of Play Tennis dataset (handle missing values, encoding, 
normalization, train-test split). '''

# Perform preprocessing (missing values, encoding, normalization, split)

import pandas as pd
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

#load the data
data=pd.read_csv("tennis.csv")
print(data.head())

#fill the missing value
simple_imputer=SimpleImputer(strategy="most_frequent")
data=pd.DataFrame(simple_imputer.fit_transform(data),columns=data.columns)

#encoding
label_encoder=LabelEncoder()
category_col=data.select_dtypes(include='object')
for col in category_col:
    data[col]=label_encoder.fit_transform(data[col])

print(data.head())

#scaling
min_max_scaler=MinMaxScaler()
number_col=data.select_dtypes(include='number')
for col in number_col:
    data[col]=min_max_scaler.fit_transform(data[[col]])

print(data.head())

#traing the model
#select the feature
x = data.drop(column=['Play Tennis'])
y = data['Play Tennis']

#splitting
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#Evalute
print("Training: ",x_train.shape)
print("Testing: ",x_test.shape)





