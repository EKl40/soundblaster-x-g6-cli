#!/bin/bash
python_bin="$(dirname $0)/../venv/bin/python"
python_file="$(dirname $0)/../src/g6_cli.py"
eval "$python_bin $python_file --set-surround Enabled --set-surround-value 25 --set-crystalizer Enabled --set-crystalizer-value 20 --set-bass Enabled --set-bass-value 10 --set-smart-volume Disabled --set-dialog-plus Disabled"
