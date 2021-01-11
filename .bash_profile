#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# start sway if running from tty1 and output to a logfile
if [ "$(tty)" = "/dev/tty1" ]; then
	exec sway 2> ~/.sway-logfile
fi
