#!/bin/bash

# This shell script generates a 'blank' setup for a new mezzanine theme.


if [ "$1" != "" ]; then
    themeName=$1
else
    themeName='myTheme'
fi

mkdir $themeName
cd $themeName
mkdir static
mkdir templates
cd static
mkdir js
mkdir css
cd ../templates
mkdir include