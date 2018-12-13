#!/usr/bin/env bash

function help {
    echo "usage: ./update arguments"
    echo "  update      Updates the packages."
    echo "  upgrade     Upgrades the packages."
}

if [ $# -eq  0 ]; then
    help
    exit 1
fi

if [ "$1" == "upgrade" ]; then
    pip-compile --upgrade requirements/base.in
    pip-compile --upgrade requirements/development.in

    pip-sync requirements/base.txt requirements/development.txt

elif [ "$1" == "update" ]; then
    pip-compile requirements/base.in
    pip-compile requirements/development.in

    pip-sync requirements/base.txt requirements/development.txt
else
    help
    exit 1
fi
