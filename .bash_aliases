# system stuff
alias sudo='sudo ' #idk what this exactly does but its useful
alias ls='exa --icons'
alias lsa='exa --icons -a'
alias lsl='exa -lhg'
alias lsla='exa -lhga'
alias c='clear'
alias grep='grep -i --color=auto'
alias update-grub='grub-mkconfig -o /boot/grub/grub.cfg'
alias watch='watch -n 0.1'

# stuff
alias gitconfig='git --git-dir=$HOME/dotfiles/ --work-tree=$HOME' #the thing for a git bare repo
alias gc='git clone'
alias yt='youtube-dl'
alias deemix='deemix -b FLAC -p ~/deemix'
alias pubip='curl ifconfig.me && echo'
alias tb='nc termbin.com 9999'
alias screen-record='wf-recorder -g "$(slurp)"'
alias upload-screenshot="wl-paste > /tmp/scr.png && 0x0 -f /tmp/scr.png"
alias cam='mpv --demuxer-lavf-format=video4linux2 --demuxer-lavf-o-set=input_format=mjpeg av://v4l2:/dev/video0 & exit'
alias mpv-cd='mpv cdda://'
alias mpv-dvd='mpv --input-cursor dvdnav://'

# commands to switcharoo the keyboard layout because sway-input wack
alias layout-hr="swaymsg input 2385:5842:Kingston_HyperX_Alloy_FPS_Pro_Mechanical_Gaming_Keyboard xkb_layout hr"
alias layout-us="swaymsg input 2385:5842:Kingston_HyperX_Alloy_FPS_Pro_Mechanical_Gaming_Keyboard xkb_layout us"

# pacman
alias pcs='sudo pacman -S'
alias pcsyu='sudo pacman -Syu'
alias pcsi='pacman -Si'
alias pcss='pacman -Ss'
alias pcscc='sudo pacman -Scc'
alias pcrs='sudo pacman -Rs'
alias pcq='pacman -Q'
alias pcqo='pacman -Qo'
alias pcqi='pacman -Qi'
alias pcqs='pacman -Qs'
# paru
alias p='paru' #running paru by itself is like an -Syu but shorter
alias prs='paru -S'
alias prsyu='paru -Syu'
alias prsi='paru -Si'
alias prss='paru -Ss'
alias prscc='paru -Scc'
alias prrs='paru -Rs'
alias prq='paru -Q'
alias prqo='paru -Qo'
alias prqi='paru -Qi'
alias prqs='paru -Qs'
