#!/bin/bash
python_bin="$(dirname $0)/../venv/bin/python"
python_file="$(dirname $0)/../src/g6_cli.py"
eval "$python_bin $python_file --sbx-surround Enabled --sbx-surround-value 50 --sbx-crystalizer Enabled --sbx-crystalizer-value 50 --sbx-bass Enabled --sbx-bass-value 30 --sbx-smart-volume Disabled --sbx-dialog-plus Disabled"
