#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# save the last 10000 commands in the ~/.bash_history file
HISTFILESIZE=10000

# easier to use my custom commands this way
export PATH="$PATH:$HOME/.local/bin"

# MPD daemon start (if no other user instance exists)
#[ ! -s ~/.config/mpd/pid ] && mpd
# not used anymore since I have the systemd user service now,
# but it's here in case someone without systemd uses this

# source the aliases
source ~/.bash_aliases

PS1="\w $ "
