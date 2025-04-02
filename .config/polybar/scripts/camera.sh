#!/bin/bash
# check if camera file exists, and print output
# (I got a physical camera switch on my laptop so this is useful)

if [[ -c "/dev/video1" ]]; then
	echo -e "%{F#ef2f27}󰄀 camera on"
else
	echo -e "%{F#918175}󰗟 camera off"
fi
