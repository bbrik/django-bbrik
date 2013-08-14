#!/bin/bash
#
# This script enters specified virtualenv and calls
# compileless management command in it

if [[ $# < 1 ]]
then
  echo "Missing virtualenv argument"
  echo "Usage:"
  echo "  compileless.sh myvirtualenv"
  exit 0
fi

source `which virtualenvwrapper.sh`
workon $1
python manage.py compileless
deactivate
