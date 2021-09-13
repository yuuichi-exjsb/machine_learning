#モジュールのインポート
from sklearn.datasets import load_boston
import numpy as np
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import mean_squared_error as MSE
import matplotlib.pyplot as plt
import openpyxl 

boston = load_boston()

X_array = boston.data
Y_array = boston.target

df = DataFrame(X_array, columns = boston.feature_names).assign(MEDV=np.array(Y_array))

X = df.loc[:,'CRIM':'LSTAT']
y = df['MEDV']
X_train,X_test,y_train,y_test = train_test_split(X,y)

#モデルの箱の準備とトレーニング用データの学習
lr = LR()
lr.fit(X_train,y_train)

#予測値の算出
y_pred_train = lr.predict(X_train)
y_pred_test = lr.predict(X_test)

#RMSEの算出
rmse_train = np.sqrt(MSE(y_train,y_pred_train))
rmse_test = np.sqrt(MSE(y_test,y_pred_test))
print(rmse_train)
print(rmse_test)

# 散布図の描画
plt.figure(figsize=(5,5))
plt.scatter(y_test,y_pred_test)

# y_test及びy_pred_testの最小値・最大値を求める
test_max = np.max(y_test)
test_min = np.min(y_test)
pred_max = np.max(y_pred_test)
pred_min = np.min(y_pred_test)

# それぞれの値を比較し、最終的な最小値・最大値を求める
max_value = np.maximum(test_max, pred_max)
min_value = np.minimum(test_min, pred_min)

# x軸およびy軸の値域を指定する
plt.xlim([min_value,max_value])
plt.ylim([min_value,max_value])

# 対角線を引く
plt.plot([min_value, max_value],[min_value,max_value])

# x軸とy軸に名前を付ける
plt.xlabel('実績値',fontname="MS Gothic")
plt.ylabel('予測値',fontname="MS Gothic")

# 可視化結果を表示する為に必要な関数
plt.show()

#MEDVの予測値と実測値をエクセルファイルに書き出し
y_pred_all = np.append(y_pred_train,y_pred_test)
y_pred_df = DataFrame(y_pred_all)
df['MEDV予測値']= y_pred_df 
df.to_excel('boston.xlsx')