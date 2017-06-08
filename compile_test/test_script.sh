#!/bin/bash
python setup.py build_ext --inplace
python compile_test/Ax_test.py

