###  Source ::  https://gist.github.com/amueller/2594372
###  http://peekaboo-vision.blogspot.in/2010/09/mnist-for-ever.html

from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold

def main():
    mnist = fetch_mldata("MNIST original")
    X_all, y_all = mnist.data/255., mnist.target
    print("scaling")
    X = X_all[:60000, :]
    y = y_all[:60000]

    X_test = X_all[60000:, :]
    y_test = y_all[60000:]

    svm = SVC(cache_size=1000, kernel='rbf')

    parameters = {'C':10. ** np.arange(5,10), 'gamma':2. ** np.arange(-5, -1)}
    print("grid search")
    grid = GridSearchCV(svm, parameters, cv=StratifiedKFold(y, 5), verbose=3, n_jobs=-1)
    grid.fit(X, y)
    print("predicting")
    print("score: ", grid.score(X_test, y_test))
    print(grid.best_estimator_)

if __name__ == "__main__":
    main()
## READ Below for understanding if __name__ == "__main__"
'''
Ref ::: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    http://ibiblio.org/g2swap/byteofpython/read/module-name.html
    https://www.guru99.com/learn-python-main-function-with-examples-understand-main.html
    
When the Python interpreter reads a source file, it executes all of the code found in it.

Before executing the code, it will define a few special variables. For example, if the python interpreter is running that
module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". 
If this file is being imported from another module, __name__ will be set to the module's name.

In the case of your script, let's assume that it's executing as the main function, e.g. you said something like

python threading_example.py
on the command line. After setting up the special variables, it will execute the import statement and load those modules. 
It will then evaluate the def block, creating a function object and creating a variable called myfunction that points to the function 
object. It will then read the if statement and see that __name__ does equal "__main__", so it will execute the block shown there.

One reason for doing this is that sometimes you write a module (a .py file) where it can be executed directly.
Alternatively, it can also be imported and used in another module. By doing the main check, you can have that code only
execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call 
your functions themselves.
'''
##  End : READ Below for understanding if __name__ == "__main__"
    
## GridSarch Example ::  https://medium.com/@aneesha/svm-parameter-tuning-in-scikit-learn-using-gridsearchcv-2413c02125a0
