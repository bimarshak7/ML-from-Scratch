import numpy as np
import matplotlib as plt

def plotDecisionBoundary(X,clf):
    '''
    Plots any two features
    X = dataset 
    clf = classifier object with decision_function() (Sklearn-> LogisticRegression, SVC)
    '''
    axes = [X[;,0].min()-2,X[;,0].max()+2,X[;,1].min()-2,X[;,1].max()+2]
    
    #plot dataset
    plt.plot(X[:, 0][y==0], X[:, 1][y==0], "bs")
    plt.plot(X[:, 0][y==1], X[:, 1][y==1], "g^")
    plt.axis(axes)
    plt.grid(True, which='both')
    plt.xlabel(r"$x_1$", fontsize=20)
    plt.ylabel(r"$x_2$", fontsize=20, rotation=0)
    
    #plot decision boundary
    x0s = np.linspace(X1m, X1mx, 100) #increase 100 to achieve more smooth boundary
    x1s = np.linspace(X2m, X2mx, 100)
    x0, x1 = np.meshgrid(x0s, x1s)
    X_ = np.c_[x0.ravel(), x1.ravel()]
    y_pred = clf.predict(X_).reshape(x0.shape)
    y_decision = clf.decision_function(X_).reshape(x0.shape)
    plt.contourf(x0, x1, y_pred, cmap=plt.cm.brg, alpha=0.2)
    plt.contourf(x0, x1, y_decision, cmap=plt.cm.brg, alpha=0.1)

#use plt.show() after function call
