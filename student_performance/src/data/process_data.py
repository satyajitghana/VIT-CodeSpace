import os
import click
import logging
from pathlib import Path
import pandas as pd

from sklearn.preprocessing import LabelEncoder


@click.command()
@click.argument('input_dir', type=click.Path())
@click.argument('output_dir', type=click.Path())
def main(input_dir, output_dir):
    """
    for processing data using command line

    :param input_dir: the directory containing the raw data
    :param output_dir: the directory containing the processed ata
    :return: None
    """

    process(input_dir, output_dir)


def process(input_dir, output_dir):
    """
    processes the data.

    :param input_dir: the directory containing the raw data
    :param output_dir: the directory containing the processed ata
    :return:
    """
    create_logger()
    logger = logging.getLogger(__name__)
    logger.info(f'making final data set from raw data. in={input_dir}, out={output_dir}')

    for (dirpath, dirnames, filenames) in os.walk(input_dir):
        for f in filenames:
            data = pd.read_csv(dirpath+f)
            one_hot_attribs = ['sex', 'address', 'Mjob', 'Fjob', 'activities', 'higher']
            encoder = LabelEncoder()

            for column in data[one_hot_attribs]:
                data[column] = encoder.fit_transform(data[column].values)

            for i, row in data.iterrows():
                if row['M1'] < 20:
                    data['M1'][i] = 0
                elif 20 <= row['M1'] < 70:
                    data['M1'][i] = 1
                else:
                    data['M1'][i] = 2

                if row['M2'] < 20:
                    data['M2'][i] = 0
                elif 20 <= row['M2'] < 70:
                    data['M2'][i] = 1
                else:
                    data['M2'][i] = 2

                if row['M3'] < 20:
                    data['M3'][i] = 0
                elif 20 <= row['M3'] < 70:
                    data['M3'][i] = 1
                else:
                    data['M3'][i] = 2
            data.to_csv(output_dir+f)

    logger.info('done')


def create_logger():
    log_fmt = '[%(levelname)s %(asctime)s]: %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]


if __name__ == '__main__':
    main()
