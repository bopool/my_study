import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# try:
#     import seaborn
#     print('Y')
# except:
#     print('n')

# mushroom = pd.read_csv('https://drive.google.com/file/d/1--RoDr9glQnWX2uJAlFRlxDZ9zhStgxS/view?usp=share_link')
# print(mushroom)

# 예제1
# print('정확도 Accuracy', ((10+895)/(10+895+90+5))*100, '%')
# print('정밀도 Precision', 10/(10+90))
# print('민감도(재현율) Sensitivity Recall', 10/(10+5))
# print('특이도 Specificity', 895/(90+895))
# print('F1', (50/15)*2)
# print('FP-Rate (1 - Specificity 예측도 실제도 다 틀린 거)', 90/(90+895))

# 예제2
# print('정확도 Accuracy', ((30+60)/(30+60+40+40))*100, '%')
# print('정밀도 Precision', 30/(30+40))
# print('민감도(재현율) Sensitivity Recall', 30/(30+40))
# print('특이도 Specificity', 60/(40+60))
# print('FP-Rate (1 - Specificity 예측도 실제도 다 틀린 거)', 40/(30+60))
# print('F1', ((0.42857**2)/(0.42857*2))*2)

import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine()

X = wine['data']
feature_names = wine['feature_names']

y = wine['target']

df = pd.DataFrame(X, columns = feature_names)
# print(df)

# print(wine['target_names'])
# print(y)
# print(y.shape)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(df['alcohol'], df['malic_acid'], c = y)
# plt.show()

pd.plotting.scatter_matrix(df, c=y, figsize =(16, 6), alpha = 0.8)
# plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,stratify = y, random_state = 777)

# print(X_train.shape, X_test.shape)
# print(y_train.shape, y_test.shape)

# print(df.describe())


# 정규화
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

scaler.fit(X_train)
X_scaled_train = scaler.transform(X_train)

pd.DataFrame(X_scaled_train).describe()
# print(a)

X_scaled_test = scaler.transform(X_test)
pd.DataFrame(X_scaled_test).describe()




from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_scaled_train, y_train)

pred_train = model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)
# print(a)

# 학습용 데이터를 만들자 // 1.0 과적합 나옴 

pred_test = model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)
#print(a)

#오차행렬 확인 

from sklearn.metrics import confusion_matrix
# print('훈련 데이터셋 오차행렬 \n', confusion_matrix(y_train, pred_train), '\n')
# print('테스트 데이터셋 오차행렬 \n', confusion_matrix(y_test, pred_test), '\n')


# 성능 결과 확인

from sklearn.metrics import classification_report
print(classification_report(y_train, pred_train))