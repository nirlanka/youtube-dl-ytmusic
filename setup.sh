#!/bin/zsh

workdir=$(pwd)
python3 -m venv $workdir/.venv
source $workdir/.venv/bin/activate

python3 -m pip install xerox

mkdir downloads
