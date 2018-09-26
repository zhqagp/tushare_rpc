#!/bin/bash
#./git.sh + commit description

if [ "! $*" ]; then
    git add . &&git commit -m fix && git push origin master
else
    git add . &&git commit -m "$*" && git push origin master
fi

