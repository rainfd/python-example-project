#!/bin/bash

APP="python-example-project"
VERSION="1.0"
REQUIRE="requirements.txt"


if [ -f $REQUIRE ]; then
    pipenv lock -r >$REQUIRE
fi

docker build . -t $APP:$VERSION
