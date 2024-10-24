"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Pfmsoft Snippets."""


if __name__ == "__main__":
    main(prog_name="pfmsoft-snippets")  # pragma: no cover
