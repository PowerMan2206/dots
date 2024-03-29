# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# source the aliases
. ~/.bash_aliases
[[ -f ~/.bash_aliases_secret ]] && . ~/.bash_aliases_secret

PS1="\w $ "
tabs -4 # non-cringe tabs
. "$HOME/.config/lf/lfcd.sh"

# search for package with command if it doesn't exist
command_not_found_handle() { 
	echo "$(tput setaf 1)Command \"$1\" doesn't exist, idiot"
	echo "It might be found in these packages:$(tput setaf 2)"
	if ! pacman -Fq "$1"; then echo "lmao there are no packages for that"; fi
	echo -n "$(tput sgr0)"
}
