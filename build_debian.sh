#!/usr/bin/env bash
# cleaning
rm deb_dist -Rfv
rm dist -Rfv
# building
python setup.py --command-packages=stdeb.command sdist_dsc --with-python2=True --with-python3=True --no-python2-scripts=True bdist_deb
