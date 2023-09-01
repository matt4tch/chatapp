#!/bin/zsh
lsof -nti:$1 | xargs kill -9