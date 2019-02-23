#!/usr/bin/env bash

function help {
    echo "usage: ./update arguments"
    echo "  update      Install pinned packages."
    echo "  upgrade     Update all packages."
}

if [ $# -eq  0 ]; then
    help
    exit 1
fi

if [ "$1" == "update" ]; then
    pip-sync requirements/base.txt requirements/development.txt

elif [ "$1" == "upgrade" ]; then
    pip-compile --upgrade requirements/base.in
    pip-compile --upgrade requirements/development.in

else
    help
    exit 1
fi
