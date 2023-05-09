# dots
Everyone must have a dotfiles repo, right?

![screenshot](https://raw.githubusercontent.com/PowerMan2206/dots/master/screenshot.png)

## Packages and stuff

package       | why
--------------|--------------
`sway`        | compositor
`foot`        | terminal
`qutebrowser` | browser
`pipewire`    | audio stuff
`bemenu`      | launcher
`waybar`      | bar
`gammastep`   | no eye hurty thing
`mpd/ncmpcpp` | music playback

Others are in `.config/packagelist`, install them with `paru -S - < packagelist` (or whatever AUR helper you have)

Note, run:
- `gsettings set org.gnome.desktop.interface gtk-theme Sweet` if the GTK theme is broken (which it most probably will be)
- `gsettings set org.gnome.desktop.interface cursor-theme win8` if the cursor is sometimes broken (again, probably is)
- `gsettings set org.gnome.desktop.wm.preferences button-layout ""` to get rid of GTK titlebars

## Installation

You can treat this repo as your home directory, so if you cloned the repo to `~/dots` you can install it by running

```
cd ~/dots
rm -rf .git README.md screenshot.png
cp -rT . ~
```

***THIS WILL OVERWRITE ANY CONFIG FILES YOU HAVE!***

Otherwise, you can just copy any specific config you want
