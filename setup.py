#-*- coding:utf-8 -*-

import setuptools
import gtagssupport as mod


setuptools.setup(
    name=mod.__name__,
    version=mod.__version__,
    install_requires=[
        'sqlalchemy',
        ],
    entry_points=dict(
        console_scripts=['gtags-lookup=gtagssupport:main']
        ))
