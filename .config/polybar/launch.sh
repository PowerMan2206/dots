#!/bin/bash
# just a thingy to restart polybar and run it on all monitors

pkill polybar

# top bar
MONITOR=eDP			polybar -c $HOME/.config/polybar/top.ini &
MONITOR=HDMI-1-1	polybar -c $HOME/.config/polybar/top.ini &

# goofy way to have the tray only on the main monitor.
# bot-notray.ini is the main one, without the tray,
# it gets sourced into bot.ini that has the tray
MONITOR=eDP			polybar -c $HOME/.config/polybar/bot.ini &
MONITOR=HDMI-1-1	polybar -c $HOME/.config/polybar/bot-notray.ini &
