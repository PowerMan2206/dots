# Dotfiles
Everyone must have a dotfiles repo, right?

![screenshot](https://raw.githubusercontent.com/PowerMan2206/dots/master/screenshot.png)

## Packages and stuff

package | why
-|-
`sway`|window manager and compositor
`alacritty`|terminal
`wofi`|launcher
`waybar`|bar
`gammastep`|screen light thing
`grim`|screenshots
`mpd`|music playback
`mpv`|video playback
[`qt5-styleplugins`](https://aur.archlinux.org/packages/qt5-styleplugins)|uniformity between Qt and GTK

other: `swayidle`, `mpc` (XF86 mpd control), `swaylock-fancy`, `noto-fonts`, `exa`

Note: the `pulseaudio-control` Waybar module config is customized to my specific setup. Go to [polybar-pulseaudio-control](https://github.com/marioortizmanero/polybar-pulseaudio-control) to see how to make it work for you.

Note 2: my Powercord theme location is a little wonky, you can move it wherever you installed Powercord/BD.

## Installation

You can treat this repo as your home directory. So if you cloned the repo to `~/dots`, for example, you can install it by running

```
cd ~/dots
rm -rf .git README.md screenshot.png
cp -rT . ~
```

**This will overwrite any previous config files you had, make sure to backup if you're running this!**

Otherwise, you can just copy any specific config you want.

### Thanks to 

[Elk o' war](https://github.com/elkowar) for helping with the `cpu-speed.sh` Waybar script

[marioortizmanero](https://github.com/marioortizmanero/polybar-pulseaudio-control) for making the `pulseaudio-control.bash` Polybar script
