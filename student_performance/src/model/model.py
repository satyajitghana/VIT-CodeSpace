import os
import click
import logging
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


@click.command()
@click.argument('data_dir', type=click.Path())
@click.option('--test', default=False)
def fit(data_dir, test=False):
    """
    for training the model (using command line). saves the model in a file

    :param data_dir: the processed data
    :param test:specifies if the model should be tested
    :return: None
    """
    create_logger()

    for (dirpath, dirnames, filenames) in os.walk(data_dir):
        for f in filenames:
            # loading data
            data = pd.read_csv(dirpath+f)

            # getting X and y vals
            X = data.drop('M3', axis=1)
            y = data['M3']

            # creating train and test sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
            logging.info(f'x_train: {X_train.shape}, x_test: {X_test.shape}, y_train: {y_train.shape}, '
                         f'y_test: {y_test.shape}')

            clf = Pipeline([
                ('reduce_dim', SelectKBest(chi2, k=2)),
                ('train', LinearSVC(C=100))
            ])

            scores = cross_val_score(clf, X_train, y_train, cv=5, n_jobs=2)
            print(f"Mean model accuracy: {np.array(scores).mean()}")

            clf.fit(X_train, y_train)

            joblib.dump(clf, "src/model/"+f[:f.find(".")]+".mdl", compress=1)

            if test:
                y_pred = clf.predict(X_test)
                print(f"Accuracy: {accuracy_score(y_test, y_pred)}")


def predict(X, subject):
    """
    uses the created model to predict the user marks.

    :param X: the information of the user
    :param subject: the model depends on the subject that is to be queried
    :return: the marks
    """

    model = joblib.load(f'src/model/{subject}.mdl')
    print(X.shape)
    return model.predict(X)


def create_logger():
    log_fmt = '[%(levelname)s %(asctime)s]: %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]


if __name__ == '__main__':
    fit()
