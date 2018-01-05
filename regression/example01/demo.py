# -*- coding:utf8 -*-
# http://blog.csdn.net/chenguolinblog/article/details/44829321
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


def get_data(file_name):
    """
    得到原始数据
    :param file_name:
    :return:
    """
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['square_feet'], data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter


def linear_model_main(X_parameters, Y_parameters, predict_value):
    """
    线性回归实现
    :param X_parameters:
    :param Y_parameters:
    :param predict_value:
    :return:
    """
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions


def show_linear_line(X_parameters, Y_parameters):
    """
    查看线性图
    :param X_parameters:
    :param Y_parameters:
    :return:
    """
    regr = linear_model.LinearRegression()
    # 训练
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters, Y_parameters, color='blue')
    plt.plot(X_parameters, regr.predict(X_parameters), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


if __name__ == '__main__':
    X, Y = get_data("data-input.csv")
    predictvalue = 700
    result = linear_model_main(X, Y, predictvalue)
    print 'Intercept value(截距值):', result['intercept']
    print 'coefficient value(系数):', result['coefficient']
    print 'Predicted value(预测值):', result['predicted_value']
    show_linear_line(X, Y)