#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

(mpv ~/walls/winxpstart.opus > /dev/null 2> /dev/null &)

# start sway if running from tty1 and output to a logfile
# also gammastep
if [ "$(tty)" = "/dev/tty1" ]; then
	gammastep -m drm -P -O 3500
	exec sway > ~/.sway-logfile
fi
