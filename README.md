# cron-expression-parser

## Installation

With `Python>=3.7` and `pip` installed (see Appendix A) run the following in the root directory of the project:

    python -m pip install .

You can now use the `cron_expression_parser` binary as described below.

## Description 
A command line application and Python library which parses a cron string and expands each field to show the times at which it will run.
Only considers the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command, and does not handle the special time strings such as "@yearly". The input is on a single line.
The cron string is passed to your application as a single argument.

    ~$ cron_expression_parser "*/15 0 1,15 * 1-5 /usr/bin/find"

The output is formatted as a table with the field name taking the first 14 columns and the times as a space-separated list following it.
For example, the following input argument:

    */15 0 1,15 * 1-5 /usr/bin/find

Yields the following output:

    minute        0 15 30 45
    hour          0
    day of month  1 15
    month         1 2 3 4 5 6 7 8 9 10 11 12
    day of week   1 2 3 4 5
    command       /usr/bin/find

## Development

Install the package in development mode:

    python -m pip install -e .[test]

To run the tests, invoke in the root directory of the project:

    pytest

## Appendix A (installing Python and pip)

Python can be installed in a multitude of fashions, depending on user needs and operating system.

One simple, portable and non-intrusive method is to install `Miniconda`, by following these steps:

### Linux

    curl https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh -o Miniconda3-py37_4.9.2-Linux-x86_64.sh
    sh Miniconda3-py37_4.9.2-Linux-x86_64.sh # interactively select target directory and such
    # follow the instructions presented by the installer to set up the shell and activate the environment
    conda install pip

### macos

    curl https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-MacOSX-x86_64.sh -o Miniconda3-py37_4.9.2-MacOSX-x86_64.sh
    sh Miniconda3-py37_4.9.2-MacOSX-x86_64.sh # interactively select target directory and such
    # follow the instructions presented by the installer to set up the shell and activate the environment
    conda install pip
