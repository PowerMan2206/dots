# Dotfiles
Everyone must have a dotfiles repo, right?

![screenshot](https://raw.githubusercontent.com/PowerMan2206/dots/master/screenshot.png)

### Note to X users

I am now using Wayland, so anything X-related isn't maintained anymore. Head into the GitHub history thing to see the X files.

## Packages and stuff

package     | why
------------|------------
`sway`      | compositor
`alacritty` | terminal
`bemenu`    | launcher
`waybar`    | bar
`gammastep` | screen light thing
`mpd`       | music playback
`mpv`       | video playback

other: look into `.config/packagelist`, install with `yay -S - < packagelist` (on Arch)

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
