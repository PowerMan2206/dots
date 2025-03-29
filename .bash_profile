[[ -f ~/.bashrc ]] && . ~/.bashrc

# variable stuff
export PATH="$HOME/.local/bin:$PATH"	# add local bin into PATH
export HISTFILESIZE=10000				# history file size
export HISTCONTROL=ignorespace			# space prefixed commands won't be added to history
export EDITOR=micro						# micro best editor fuck you bread

# if on tty1, run i3
if [ "$(tty)" = "/dev/tty1" ]; then
	exec startx
fi
