"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Big Data Analytics."""


if __name__ == "__main__":
    main(prog_name="big-data-analytics")  # pragma: no cover
