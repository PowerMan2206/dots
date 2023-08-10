[[ -f ~/.bashrc ]] && . ~/.bashrc
[[ ! -d ~/.sway-logs ]] && mkdir ~/.sway-logs

# variable stuff
#export QT_QPA_PLATFORMTHEME=
#export QT_QPA_PLATFORM=
export PATH="$PATH:$HOME/.local/bin"	#add local bin into PATH
export HISTFILESIZE=10000				#history file size
export HISTCONTROL=ignorespace			#space prefixed commands won't be added to history
export EDITOR=micro						#micro best editor fuck you bread

date=$(date +"%Y-%m-%d_%H:%M:%S") #for the thing below
# start sway if running from tty1 and output to logfiles
if [ "$(tty)" = "/dev/tty1" ]; then
	tldr -u &
	# for some reason I don't need this anymore but it'll be here in case I do in the future again
	# fuk u nvidia
	#WLR_DRM_NO_MODIFIERS=1 
	#WLR_NO_HARDWARE_CURSORS=1
	exec sway -d \
	> ~/.sway-logs/sway-log-"$date".log \
	2> ~/.sway-logs/sway-log2-"$date".log
fi
