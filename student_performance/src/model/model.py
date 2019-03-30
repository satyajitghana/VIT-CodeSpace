import click
import logging
import pickle
from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


@click.command()
@click.argument('datafile', type=click.File())
@click.option('--test', default=False)
def fit(datafile, test=False):
    """
    for training the model (using command line). saves the model in a file

    :param datafile: the processed data
    :param test:specifies if the model should be tested
    :return: None
    """
    create_logger()

    # loading data
    data = pd.read_csv(datafile)

    # getting X and y vals
    X = data.drop('M3', axis=1).values
    y = data['M3'].values

    # creating train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    logging.info(f'x_train: {X_train.shape}, x_test: {X_test.shape}, y_train: {y_train.shape}, y_test: {y_test.shape}')

    # creating model
    model = LogisticRegression()

    # training
    model.fit(X_train, y_train)
    datafile_name = datafile.name
    pickle.dump(model, open("src/model/"+datafile_name[datafile_name.rfind("/")+1:datafile_name.find(".")]+".mdl", "wb"))

    if test:
        y_pred = model.predict(X_test)
        print(f"Accuracy: {accuracy_score(y_test, y_pred)}")


def predict(X):
    """
    uses the created model to predict the user marks.

    :param X: the information of the user
    :return: the marks
    """

    # model = pickle.load(open('src/model/'))
    pass


def create_logger():
    log_fmt = '[%(levelname)s %(asctime)s]: %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]


if __name__ == '__main__':
    fit()
