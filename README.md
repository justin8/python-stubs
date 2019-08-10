# Python Stubs

This repo contains some stub python packages to quickly make a particular type of python package quickly and painlessly without having to remember how to do all the boilerplate.

## Setup:
`pip install -r requirements.txt`

## Usage
```
./create.py --author "Justin Dray" --email "justin@dray.be" --output-dir /tmp/foo --package-name something
cd /tmp/foo
pip install -e .
```

Now your package "something" is created in the folder "/tmp/foo", and is installed with pip in development mode.

Tests are also included, just run `./setup.py test` to run them.

## Current Templates:

### cli
This template is for a basic CLI command, using click for the interface. Once created and installed with pip, you can call your package from your shell using the name of the package
