#!/bin/bash


# virtualenv --system-site-packages dpp
PROJ=rescue

VIRTUALENV=$WORKON_HOME/$PROJ/
if [ ! -d "$VIRTUALENV" ];
then
    echo "Creating $PROJ virtual environment..."
    virtualenv --system-site-packages $PROJ
fi

workon $PROJ

HCLIB=$WORKON_HOME/$PROJ/lib/python2.7/site-packages/hardlycode
if [ ! -d "$HCLIB" ];
then
    echo "Linking hardlycode library..."
    ln -s ~/projects/python/hardlycode-lib/hardlycode $HCLIB
fi

if [ ! -d "static" ];
then
    echo "Making static directory..."
    mkdir static
fi

pip install -r requirements.txt
python manage.py collectstatic
python manage.py syncdb
python manage.py runserver