import click
import logging
from pathlib import Path


@click.command()
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path())
def main(input_dir, output_dir):
    """
    for processing data using command line

    :param input_dir: the directory of the raw data
    :param output_dir: the directory of the processed ata
    :return: None
    """

    process(input_dir, output_dir)


def process(input_dir, output_dir):
    """
    processes the data.

    :param input_dir: the directory of the raw data
    :param output_dir: the directory of the processed ata
    :return:
    """
    create_logger()
    logger = logging.getLogger(__name__)

    logger.info(f'making final data set from raw data. in={input_dir}, out={output_dir}')
    # do stuff
    logger.info('done')


def create_logger():
    log_fmt = '[%(levelname)s %(asctime)s]: %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]


if __name__ == '__main__':
    main()
