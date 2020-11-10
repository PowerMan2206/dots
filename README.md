# Dotfiles
Everyone must have a dotfiles repo, right?

## Packages and stuff

package | why
-|-
`i3-gaps`|take a wild, wild guess
`alacritty`|terminal
[`picom-ibhagwan-git`](https://github.com/ibhagwan/picom) ([AUR](https://aur.archlinux.org/packages/picom-ibhagwan-git))|compositor
`rofi`|launcher
`nitrogen`|wallpapers
`polybar`|bar
`redshift`|screen light thing
`scrot`|screenshots
`mpd`|music playback

other: `xorg-setxbmap`, `xorg-xinput`, `mpc`, `xclip`

## Installation

You can treat this repo as your home directory. So if you cloned the repo to `~/dotfiles`, for example, you could install it by simply running

```
cp -rT ~/dotfiles/ ~
```

**Note: this will overwrite any previous config files you had, make sure to backup if you're running this!**

Otherwise, you can just copy any specific config you want.

### Thanks to 
[exorcist](https://gitlab.com/exo-git/fonts/-/tree/master/hack-fonts) for the Hack Nerd font

[Elk o' war](https://github.com/elkowar) for helping with the `cpu-speed.sh` Polybar script
