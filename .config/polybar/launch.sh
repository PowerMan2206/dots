# I have no idea how this works, but basically 
# it just runs Polybar on each of your monitors

if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1 | tac); do
    MONITOR=$m polybar --reload main -c ~/.config/polybar/config.ini &
  done
else
  polybar --reload main -c ~/.config/polybar/config.ini &
fi
