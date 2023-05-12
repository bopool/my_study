import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', size = 14)
import seaborn as sns

sns.set(style = 'white')
sns.set(style = 'whitegrid', color_codes = True)

import warnings
warnings.simplefilter(action = 'ignore')

train_df = pd.read_csv('titanic/train.csv')
test_df = pd.read_csv('titanic/test.csv')

print(len(train_df), len(test_df))

# 결측치 확인 
print(train_df.isnull().sum())

# 결측치 비율
print('Percent of missing "Age" records is %.2f%%' %((train_df['Age'].isnull().sum()/ train_df.shape[0])*100))

# Age를 분석해 보자. 

ax = train_df['Age'].hist(bins=15, density = True, stacked = True, color = 'teal', alpha = 0.6)
train_df['Age'].plot(kind = 'density', color = 'teal')
ax.set(xlabel = 'Age')
plt.xlim(-10, 85)
plt.show()

# 결측치를 무시할지 여부 
print('The mean of "Age" is %.2f' %(train_df['Age'].mean(skipna = True)))
print('The median of "Age" is %.2f' %(train_df['Age'].median(skipna = True)))
print('The mode of "Age" is %.2f' %(train_df['Age'].mode()))

print('Persent of missing "Embarked" recods is %.2f%%' %((train_df['Embarked'].isnull().sum())))
print('Percent of missing "Cabin" recaords is %.2f%%' %((train_df['Cabin'].isnull().sum()/ train_df.shape[0])*100))
print('Boarded passengers grouped by port of embarkeation (C = Cherbourg, Q = Queenstown, S= Southhampton)')
print(train_df['Embarked'].value_counts())


sns.countplot(x = 'Embarked', data = train_df, palette = 'Set2')
plt.show()

# 결측치 처리 
train_data = train_df.copy()
train_data['Age'].fillna(train_data['Age'].median(skipna = True), inplace = True)
train_data['Embarked'].fillna(train_data['Embarked'].value_counts().idxmax(), inplace = True)
train_data.drop('Cabin', axis = 1, inplace = True)

print(train_data.isnull().sum())

# 결측치 처리 전과 처리 후의 figure
plt.figure(figsize = (15, 8))
ax = train_df['Age'].hist(bins = 15, density = True, stacked = True, color = 'teal', alpha = 0.6)
train_df['Age'].plot(kind = 'density', color = 'teal')
ax = train_data['Age'].hist(bins = 15, density = True, stacked = True, color = 'orange', alpha = 0.5)
train_data['Age'].plot(kind = 'density', color = 'orange')
ax.legend(['Raw Age', 'Adjusted Age'])
ax.set(xlabel = 'Age')
plt.xlim(-10, 85)
plt.show()


train_data['TravelAlone'] = np.where((train_data['SibSp']+train_data['Parch']) > 0, 0, 1)
train_data.drop('SibSp', axis = 1, inplace = True)
train_data.drop('Parch', axis = 1, inplace = True)

training = pd.get_dummies(train_data, columns = ['Pclass', 'Embarked', 'Sex'])
training.drop('PassengerId', axis = 1, inplace = True)
training.drop('Name', axis = 1, inplace = True)
training.drop('Ticket', axis = 1, inplace = True)

final_train = training 
training.head()

# test에도 똑같이 적용해줘야 한다. 

test_data = test_df.copy()
test_data['Age'].fillna(train_data['Age'].median(skipna = True), inplace = True)
test_data['Embarked'].fillna(train_data['Embarked'].value_counts().idxmax(), inplace = True)
test_data.drop('Cabin', axis = 1, inplace = True)

testing = pd.get_dummies(train_data, columns = ['Pclass', 'Embarked', 'Sex'])
testing.drop('PassengerId', axis = 1, inplace = True)
testing.drop('Name', axis = 1, inplace = True)
testing.drop('Ticket', axis = 1, inplace = True)

final_test = testing 
testing.head()


print(final_train.columns)

plt.figure(figsize = (15, 8))
az = sns.kdeplot(final_train['Age'][final_train.Survived == 1], color = 'darkturquoise', shade = True)
sns.kdeplot(final_train['Age'][final_train.Survived == 0], color = 'lightcoral', shade = True)
plt.legend(['Survived', 'Died'])
plt.title('Desity Plot of Age for Surviving Population and Deceased Population')
ax.set(xlabel = 'Age')
plt.xlim(-10, 85)
plt.show()

# age, Survived -> plot

plt.figure(figsize = (20, 8))
avg_survival_byage = final_train[['Age', 'Survived']].groupby(['Age'], as_index = False).mean()

g = sns.barplot(x = 'Age', y = 'Survived', data = avg_survival_byage, color = 'LightSeaGreen')
plt.show()


# ISMinor

final_train['ISMinor'] = np.where(final_train['Age'] < 16, 1, 0)
final_test['ISMinor'] = np.where(final_test['Age'] < 16, 1, 0)

# Exploration of Fare
plt.figure(figsize = (15, 8))
ax = sns.kdeplot(final_train['Fare'][final_train.Survived == 1], color = 'darkturquoise', shade = True)
sns.kdeplot(final_train['Fare'][final_train.Survived == 0], color = 'lightcoral', shadow = True)
plt.legend(['Survived', 'Died'])
plt.title('Density Plot of Fare for Surviving Population and Deceased Population')
ax.set(xlabel = 'Fare')
plt.xlim(-10, 85)
plt.show()


sns.barplot(data = train_df, x = 'Pclass', y = 'Survived', color = 'darkturquoise')
plt.show()

sns.barplot(data = train_df, x = 'Embarked', y = 'Survived', color = 'darkturquoise')
plt.show

sns.barplot(data = final_train, x = 'TravelAlone', y = 'Survived', color = 'darkturquoise')
plt.show()

# Logistic Regression 논리적 진압

from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

cols = ['Age', 'Fare', 'TravelAlone', 'Pclass_1', 'Pclass_2', 'Embarked_C', 'Embarked_S', 'ISMinor']
X = final_train[cols]
y = final_train['Survived']

model = LogisticRegression()

rfe = RFE(model, n_features_to_select = 5) # feature Ranking
rfe = rfe.fit(X, y)
print('Selected features: %s' %list(X.columns[rfe.support_]))

print(final_train.columns)

# RFE+CV

from sklearn.feature_selection import RFECV
rfecv = RFECV(estimator = LogisticRegression(), step = 1, cv = 10, scoring = 'accuracy')
rfecv.fit(X, y)

print('Optimal number of features: %d' % rfecv.n_features_)
print('Selected features: %s' % list(X.columns[rfecv.support_]))

# Plot number of features VS. cross-validation scores

plt.figure(figsize = (10, 6))
plt.xlabel('Number of features selected')
plt.ylabel('Cross vaildation score (nb of correct classifications)')
plt.plot(range(1, len(rfecv.cv_results_['mean_test_score']) + 1), rfecv.cv_results_['mean_test_score'])
plt.show()


Selected_features = ['Age', 'TravelAlone', 'Pclass_1', 'Pclass_2', 'Embarked_C', 'Embarked_S', 'ISMinor']
X = final_train[Selected_features]

plt.subplots(figsize = (8, 5))
sns.heatmap(X.corr(), annot = True, cmap = 'RdYlGn')
plt.show()

