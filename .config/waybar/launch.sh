#!/bin/bash

# kill running bars and other stuff
pkill -9 waybar
pkill -9 mpdvol
pkill -9 mpc

#run bars
waybar -c ~/.config/waybar/config-bottom &
waybar -c ~/.config/waybar/config-top &
