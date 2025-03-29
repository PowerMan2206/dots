#!/bin/bash

touch /tmp/current-sink

while
	sleep 0.05 # give it a lil time to do whatever
	sink="$(pactl get-default-sink)"
	case "$sink" in
		"alsa_output.pci-0000_34_00.6.analog-stereo" ) echo "󰋋 Internal" ;;
		"alsa_output.pci-0000_01_00.1.hdmi-stereo" ) echo "󰍹 Monitor" ;;
		"alsa_output.usb-Burr-Brown_from_TI_USB_Audio_CODEC-00.analog-stereo-output" ) echo "󰓃 Behringer UMC22" ;;
		* ) echo "$sink" ;;
	esac
do ! inotifywait -qq /tmp/current-sink; done
