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
`pipewire`  | audio stuff
`bemenu`    | launcher
`waybar`    | bar
`gammastep` | screen light thing
`mpd`       | music playback
`mpv`       | video playback

other: look into `.config/packagelist`, install with `paru -S - < packagelist` (on Arch)

Note: the `pipewire-control` Waybar module is customized to my specific setup. Read into the script to see how to make it work for you.

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

[Elk o' war](https://github.com/elkowar) for helping with the `cpu-speed.sh` Waybar script.

The boys over on IRC for helping me with the `pipewire-control` Waybar script.
