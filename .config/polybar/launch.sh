# I have no idea how this works, but basically 
# it just runs Polybar on each of your monitors

# kill running polybar
pkill polybar

# run bottom polybar
for m in $(xrandr --query | grep " connected" | cut -d" " -f1 | tac); do
	MONITOR=$m polybar --reload main -c ~/.config/polybar/config-bottom.ini &
done

# run top polybar
for m in $(xrandr --query | grep " connected" | cut -d" " -f1 | tac); do
	MONITOR=$m polybar --reload main -c ~/.config/polybar/config-top.ini &
done
