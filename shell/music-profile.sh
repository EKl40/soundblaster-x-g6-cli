#!/bin/bash
python_bin="$(dirname $0)/../venv/bin/python"
python_file="$(dirname $0)/../g6_cli.py"
eval "$python_bin $python_file --set-surround Enabled --set-surround-value 50 --set-crystalizer Enabled --set-crystalizer-value 50 --set-bass Enabled --set-bass-value 30 --set-smart-volume Disabled --set-dialog-plus Disabled"
