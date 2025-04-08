#!/bin/bash
# copy the date, time, or both to clipboard with different mouse keys

case $1 in
	"date" )
		date +"%Y-%m-%d" | tr -d '\n' | xclip -selection c
		notify-send "date copied"
		;; 
	"time" )
		date +"%H:%M:%S" | tr -d '\n' | xclip -selection c
		notify-send "time copied"
		;;
	"both" )
		date +"%Y-%m-%d %H:%M:%S" | tr -d '\n' | xclip -selection c
		notify-send "both copied"
		;;
esac
