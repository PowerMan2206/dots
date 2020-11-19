# Dotfiles
Everyone must have a dotfiles repo, right?

![screenshot](https://raw.githubusercontent.com/PowerMan2206/dots/master/.config/old-x-bloat/screenshot.png)

# THIS IS NO LONGER MAINTAINED!

I have switched to Wayland, so this directory is like an archive of what my dots looked like before. Don't expect any more updates to this.

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
`mpv`|video playback
[`qt5-styleplugins`](https://aur.archlinux.org/packages/qt5-styleplugins)|uniformity between Qt and GTK

other: `xorg-setxbmap`, `xorg-xinput`, `xautolock`, `mpc` (XF86 mpd control), [`i3lock-fancy`](https://github.com/meskarune/i3lock-fancy) ([AUR](https://aur.archlinux.org/packages/i3lock-fancy-git)), `noto-fonts`, `unclutter`, `exa`

Note: the `pulseaudio-control` Polybar module config is customized to my specific setup. Go to [polybar-pulseaudio-control](https://github.com/marioortizmanero/polybar-pulseaudio-control) to see how to make it work for you.

Note 2: my Powercord theme location is a little wonky, you can move it wherever you installed Powercord/BD.

## Installation

You can treat this repo as your home directory. So if you cloned the repo to `~/dots`, for example, you can install it by running

```
cd ~/dots
rm -rf .git README.md screenshot.png
cp -rT . ~
```

**Note: this will overwrite any previous config files you had, make sure to backup if you're running this!**

Otherwise, you can just copy any specific config you want.

### Thanks to 

[Elk o' war](https://github.com/elkowar) for helping with the `cpu-speed.sh` Polybar script

[marioortizmanero](https://github.com/marioortizmanero/polybar-pulseaudio-control) for making the `pulseaudio-control.bash` Polybar script
