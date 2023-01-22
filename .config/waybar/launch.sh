#!/bin/bash

# kill running bars
pkill -9 waybar

# run bars
waybar -c ~/.config/waybar/bot &
waybar -c ~/.config/waybar/top &
