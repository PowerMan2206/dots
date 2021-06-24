#!/bin/bash

# kill running bars
pkill -9 waybar

#run bars
waybar -c ~/.config/waybar/config-bottom &
waybar -c ~/.config/waybar/config-top &
