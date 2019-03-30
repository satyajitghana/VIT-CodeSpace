import click


@click.command()
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path())
def query(input_dir, output_dir):
    print("WORKSSSS!!")
