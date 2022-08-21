#!/bin/zsh
export CONV_PATH=$PWD/../.venv/lib/python3.8/site-packages/vb2py
cd $CONV_PATH
python converter.py -c -f $1 $2