#!/bin/bash

# This shell script generates a 'blank' setup for a new mezzanine theme.
#
# To use it, type theme.sh yourNewThemeName
# If you just type theme.sh, it will create a theme with the name 'myTheme'.
#

if [ "$1" != "" ]; then
    themeName=$1
else
    themeName='myTheme'
fi

cd mezzanine_themes
mkdir $themeName
cd $themeName
mkdir static
mkdir templates
cd static
mkdir js
mkdir css
cd ../templates
mkdir include
