[[ -f ~/.bashrc ]] && . ~/.bashrc

(mpv ~/walls/winxpstart.opus &> /dev/null &)

# start sway if running from tty1 and output to a logfile
# also gammastep
if [ "$(tty)" = "/dev/tty1" ]; then
	gammastep -m drm -P -O 3500
	WLR_DRM_NO_MODIFIERS=1 exec sway -d > ~/.sway-logfile 2> ~/.sway-logfile2
fi
