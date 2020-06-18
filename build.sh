#!/bin/bash

APP="python-example-project"
VERSION="1.0"
REQUIRE="requirements.txt"


test -f $REQUIRE || pipenv lock -r >$REQUIRE

docker build . -t $APP:$VERSION
