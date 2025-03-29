# system stuff
# I can't be bothered to properly remember these
alias sudo='sudo ' #idk what this exactly does but its useful
alias cat='bat -pp' #haha pp
alias ls='exa --icons'
alias lsa='exa --icons -a'
alias lsl='exa -lhg'
alias lsal='exa -lhga'
alias lsla='exa -lhga'
alias c='clear'
alias grep='grep -i --color=auto'
alias watch='watch -n 0.5'
alias rm='echo "use rb retard"; false'
alias rb='trash-put' #because tr is taken so its like "rubbish"

# stuff
alias gitconfig='git --git-dir=$HOME/dotfiles/ --work-tree=$HOME' #the thing for a git bare repo
alias gc='git clone'
alias pubip='(curl ifconfig.me && echo)'
alias tb='nc termbin.com 9999'
alias lofi='mpv --no-video https://youtu.be/jfKfPfyJRdk'
alias synth='mpv --no-video https://youtu.be/4xDzrJKXOOY'
alias cam='mpv --demuxer-lavf-o=video_size=1280x720,input_format=mjpeg,framerate=30 --untimed av://v4l2:/dev/video0'
alias lf='lfcd'
alias notes='$EDITOR ~/notes'
alias neofetch='fastfetch' #lol

# pacman
alias pcs='sudo pacman -S'
alias pcsi='pacman -Si'
alias pcss='pacman -Ss'
alias pcrs='sudo pacman -Rs'
alias pcq='pacman -Q'
alias pcqo='pacman -Qo'
alias pcqi='pacman -Qi'
alias pcqs='pacman -Qs'
# paru
alias p='paru' #running paru by itself is like an -Syu but shorter
alias prs='paru -S'
alias prsi='paru -Si'
alias prss='paru -Ss'
alias prscc='paru -Scc'
alias prrs='paru -Rs'
alias prq='paru -Q'
alias prqo='paru -Qo'
alias prqi='paru -Qi'
alias prqs='paru -Qs'
