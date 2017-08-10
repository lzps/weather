#!/usr/bin/env python3
# coding: utf-8
import os


def lib_list():
    t = os.listdir(os.path.split(os.path.realpath(__file__))[0])
    t.remove('lib.py')
    t.remove('__init__.py')
    if '__pycache__' in t:
        t.remove('__pycache__')
    return [x.split('.')[0] for x in t]
