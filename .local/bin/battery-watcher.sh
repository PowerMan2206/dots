#!/bin/bash

batdir="/sys/class/power_supply/BAT0"

while true; do
	if [[ "$(cat ${batdir}/status)" == "Discharging" ]]; then
		case $(cat "$batdir/capacity") in
			30 ) notify-send "Battery at 30%" ;;
			20 ) notify-send "Battery at 20%" ;;
			10 ) notify-send -u critical "charge your laptop retard, 10%" ;;
		esac
	fi
	sleep 30
done
