[[ -f ~/.bashrc ]] && . ~/.bashrc

(mpv ~/walls/winxpstart.opus &> /dev/null &)
date=$(date +"%Y-%m-%d_%H:%M:%S")

# environment variable stuff
export QT_QPA_PLATFORMTHEME=qt5ct

# start sway if running from tty1 and output to logfiles
# also gammastep
if [ "$(tty)" = "/dev/tty1" ]; then
	gammastep -m drm -P -O 3500
	WLR_DRM_NO_MODIFIERS=1 exec sway -d \
	> ~/.sway-logs/sway-log-"$date" \
	2> ~/.sway-logs/sway-log2-"$date"
fi
