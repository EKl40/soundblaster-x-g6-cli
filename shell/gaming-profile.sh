#!/bin/bash
python_bin="$(dirname $0)/../venv/bin/python"
python_file="$(dirname $0)/../src/g6_cli.py"
eval "$python_bin $python_file --sbx-surround Enabled --sbx-surround-value 25 --sbx-crystalizer Enabled --sbx-crystalizer-value 20 --sbx-bass Enabled --sbx-bass-value 10 --sbx-smart-volume Disabled --sbx-dialog-plus Disabled"
