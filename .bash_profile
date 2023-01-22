[[ -f ~/.bashrc ]] && . ~/.bashrc

# setup stuff
export QT_QPA_PLATFORMTHEME=c0ck4ndb41170r7ur3 #can be litarally whatever
export QT_QPA_PLATFORM=
export PATH="$PATH:$HOME/.local/bin"
export HISTFILESIZE=10000
export EDITOR=micro
date=$(date +"%Y-%m-%d_%H:%M:%S")

# start sway if running from tty1 and output to logfiles
if [ "$(tty)" = "/dev/tty1" ]; then
	tldr -u &
	# for some reason I don't need this anymore but it'll be here in case I do in the future again
	# fuk u nvidia
	#WLR_DRM_NO_MODIFIERS=1 
	WLR_NO_HARDWARE_CURSORS=1 \
	exec sway -d \
	> ~/.sway-logs/sway-log-"$date" \
	2> ~/.sway-logs/sway-log2-"$date"
fi
