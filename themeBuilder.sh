#!/bin/bash

# This shell script generates a 'blank' setup for a new mezzanine theme.


#echo "Hello World!"
mkdir $1
cd $1
mkdir static
mkdir templates
cd static
mkdir js
mkdir css
