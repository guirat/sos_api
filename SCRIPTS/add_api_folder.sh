#!/bin/sh
echo "Please enter the folder's name"
read url
cd $url
mkdir api
cd api
touch __init__.py serializers.py urls.py views.py
cd ..
