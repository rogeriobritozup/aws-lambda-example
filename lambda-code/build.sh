#!/bin/bash

echo -e "removing build folder..."
[ -e ./build ] && rm -r ./build

echo -e "creating build folder..."
mkdir build

echo -e "instaling dependencies..."
pip install --target ./build -r ./requirements.txt

echo -e "copying py files to build folder"
cp ./*.py ./build

echo -e "generating build.zip file"
cd ./build && zip -r ./build.zip * && cd ..