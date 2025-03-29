#!/bin/bash

# in case of rerunning the script
pkill xob

# where the pipes will be
brififo="/tmp/xob-brightness"
volfifo="/tmp/xob-volume"

# make xob pipes if not there
if [[ ! -p $brififo ]]; then mkfifo $brififo; fi
if [[ ! -p $volfifo ]]; then mkfifo $volfifo; fi

# run xobs with 1.5s timeout
tail -f $brififo | xob -q -t 1500 -s brightness &
tail -f $volfifo | xob -q -t 1500 -s volume &
