#!/bin/bash
# just a thingy to restart polybar and run it on all monitors

pkill polybar

# top bar
MONITOR=eDP			polybar -c $HOME/.config/polybar/top.ini &
MONITOR=HDMI-1-1	polybar -c $HOME/.config/polybar/top.ini &

# goofy way to have the tray only on the main monitor.
# bot-main.ini is the main one, without the tray,
# it gets sourced into bot1.ini and bot2.ini (1 has, 2 doesn't have the tray)
MONITOR=eDP			polybar -c $HOME/.config/polybar/bot1.ini &
MONITOR=HDMI-1-1	polybar -c $HOME/.config/polybar/bot2.ini &
