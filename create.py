#!/usr/bin/env python3

import click
import os
import shutil
import logging
from pathlib import Path
from jinja2 import Template

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

@click.command()
@click.option("--author", required=True)
@click.option("--email", required=True)
@click.option("--license", default="MIT", help="Default value: 'MIT'")
@click.option("--output-dir", required=True)
@click.option("--package-name", required=True)
@click.option("--template", default="cli")
@click.option("--url", default="")
def entrypoint(author, email, license, output_dir, package_name, template, url):
    template_path = Path().joinpath(os.getcwd(), template)
    output_dir = Path(output_dir)

    logger.info(f"Copying template {template_path} to {output_dir}")
    shutil.copytree(template_path, output_dir)

    logger.info("Iterating over templates...")
    for input_file in output_dir.rglob("*"):
        if input_file.suffix == ".jinja":
            logger.info(f"Found template {input_file}")
            output_file = input_file.with_suffix("")
            with input_file.open() as f:
                input_data = Template(f.read())
            with output_file.open("w") as f:
                f.write(input_data.render(
                    author=author,
                    email=email,
                    license=license,
                    package_name=package_name,
                    url=url,
                    ))
            os.remove(input_file)

    logger.info(f"Renaming src dir to {package_name}")
    shutil.move(output_dir.joinpath("src"), output_dir.joinpath(package_name))

    logger.info(f"Marking setup.py as executable...")
    output_dir.joinpath("setup.py").chmod(0o755)

    logger.info(f"Complete!")


if __name__ == "__main__":
    entrypoint()
