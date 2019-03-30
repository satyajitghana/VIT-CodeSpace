import click
import logging
from pathlib import Path


@click.command()
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path())
def main(input_dir, output_dir):
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    # do stuff
    logger.info('done')


if __name__ == '__main__':
    log_fmt = '[%(levelname)s %(asctime)s]: %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    main()
