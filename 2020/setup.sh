#!/bin/sh

readonly day=$1
readonly folder="day${day}"

mkdir -p "day${day}"
cp template.py ${folder}/day${day}.py
touch ${folder}/input
