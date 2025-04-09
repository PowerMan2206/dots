#!/bin/bash
# check some stuff and print their status

case $1 in
	# (I got a physical camera switch on my laptop so this is useful)
	
	"camera" )
		if [[ -c "/dev/video1" ]]; then
			echo -e "%{F#ef2f27}%{O1}󰄀 %{O-1}"
		else
			echo -e "%{F#918175}󰗟 "
		fi
		;;
		
	"airplane" )
		# check NM status and see if wifi is off
		# (thus, airplane mode on)
		
		if [[ "$(nmcli radio wifi)" == "disabled" ]]; then
			# offsets because the 2 icons aren't centered
			echo -e "%{F#ef2f27}%{O1}󰀝 %{O-1}"
		else
			echo -e "%{F#918175}󰀞 "
		fi
		;;
	
	"microphone" )
		# pretty self-explanitory
		
		if [[ "$(pamixer --source "alsa_input.pci-0000_34_00.6.analog-stereo" --get-mute)" == "true" ]]; then
			echo -e "%{F#918175}󰍭 "
		else
			echo -e "%{F#519f50} "
		fi
		;;
esac

