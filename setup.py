#! /usr/bin/python

from distutils.core import setup
import py2exe
import os

setup(
    name='LastScrape GUI',
    version='0.1',
    description='LastScrape GUI for libre.fm',
    author='Petr Viktorin',
    author_email='encukou@gmail.com',
    url='http://encukou.cz/petr/lastscrapegui/',
    packages=['lastscrape'],
    license="GPLv3",
    zipfile='library.zip',
    windows=[{
        'script': '__init__.py',
        "dest_base": "lastscrape",
    }],
    options=dict(
        py2exe={
            "includes": ["sip", "elementtree.ElementTree"],
            "excludes": ["Tkconstants","Tkinter","tcl","doctest","pdb","unittest","difflib","inspect"],
            "compressed": 1,
            "optimize": 0,
        },
    ),
    package_dir={'lastscrape': ''},
    data_files=[ ("",["lastscrape.ui", "vcredist_x86.exe"])], requires=['PyQt4', 'PyQt4', 'py2exe']
)
