#!/bin/bash
# goes to next PulseAudio sink
# (C) 2022, @j2L4e, MIT License
# https://gist.github.com/j2L4e/ae1042fc5968225fc3b6095d670fe273

# for current-sink.sh
touch /tmp/current-sink

currentline=$(pactl list short sinks | grep -n "$(pactl get-default-sink)" | cut -d: -f 1)
lastline=$(pactl list short sinks | wc -l)
nextline=$(($currentline % $lastline + 1))
nextsink=$(pactl list short sinks | head "-n$nextline" | tail -1 | cut -f 1)

pactl set-default-sink "$nextsink"

for sinkinput in $(pactl list short sink-inputs | cut -f 1); do
  pactl move-sink-input "$sinkinput" "@DEFAULT_SINK@"
done
