#system stuff
alias sudo='sudo ' #idk what this exactly does but its useful
alias ls='exa'
alias c='clear'
alias grep='grep -i --color=auto'
alias update-grub='grub-mkconfig -o /boot/grub/grub.cfg'

#stuff
alias micro='micro -colorscheme simple'
alias yt='youtube-dl'
alias yt-opus='youtube-dl --extract-audio --audio-format=opus'
alias gc='git clone'
alias gitconfig='git --git-dir=$HOME/dotfiles/ --work-tree=$HOME' #the thing for a git bare repo
alias pubip='curl ifconfig.me'
alias tb='nc termbin.com 9999'
alias screen-record='wf-recorder -g "$(slurp)"'
alias w2x='waifu2x-ncnn-vulkan'

#commands to switcharoo the keyboard layout because sway-input wack
alias layout-hr="swaymsg input 2385:5842:Kingston_HyperX_Alloy_FPS_Pro_Mechanical_Gaming_Keyboard xkb_layout hr"
alias layout-us="swaymsg input 2385:5842:Kingston_HyperX_Alloy_FPS_Pro_Mechanical_Gaming_Keyboard xkb_layout us"

#pacman
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
#paru
alias p='paru' #running paru by itself is like an -Syu but shorter
alias ps='paru -S' #if you wanna use actual `ps` just run `command ps`
alias psyu='paru -Syu'
alias psi='paru -Si'
alias pss='paru -Ss'
alias pscc='paru -Scc'
alias prs='paru -Rs'
alias pq='paru -Q'
alias pqo='paru -Qo'
alias pqi='paru -Qi'
alias pqs='paru -Qs'
