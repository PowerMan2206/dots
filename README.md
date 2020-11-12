# Dotfiles
Everyone must have a dotfiles repo, right?

![screenshot](https://raw.githubusercontent.com/PowerMan2206/dots/master/screenshot.png)

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
`flameshot`|screenshots
`mpd`|music playback
[`qt5-styleplugins`](https://aur.archlinux.org/packages/qt5-styleplugins)|uniformity between Qt and GTK

other: `xorg-setxbmap`, `xorg-xinput`, `xautolock`, `mpc` (XF86 mpd control), `scrot` (i3lock), `noto-fonts`

## Installation

You can treat this repo as your home directory. So if you cloned the repo to `~/dotfiles`, for example, you can install it by running

```
cd ~/dotfiles
rm -rf .git README.md screenshot.png
cp -rT . ~
```

**Note: this will overwrite any previous config files you had, make sure to backup if you're running this!**

Otherwise, you can just copy any specific config you want.

### Thanks to 

[Elk o' war](https://github.com/elkowar) for helping with the `cpu-speed.sh` Polybar script
