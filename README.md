# Dotfiles
Everyone must have a dotfiles repo, right?

![screenshot](https://raw.githubusercontent.com/PowerMan2206/dots/master/screenshot.png)

## packages and stuff

package       | why
--------------|------------
`sway`        | compositor
`alacritty`   | terminal
`qutebrowser` | browser
`pipewire`    | audio stuff
`bemenu`      | launcher
`waybar`      | bar
`gammastep`   | screen light thing
`mpd`         | music playback
`mako`        | notifications

other: look into `.config/packagelist`, install with `paru -S - < packagelist` (on Arch)

note, run:
- `gsettings set org.gnome.desktop.interface gtk-theme Sweet` if the GTK theme is broken (which it most probably will be)
- `gsettings set org.gnome.desktop.interface cursor-theme win8` if the cursor is sometimes broken (again, probably is)
- `gsettings set org.gnome.desktop.wm.preferences button-layout ""` to get rid of GTK titlebars

## installation

you can treat this repo as your home directory, so if you cloned the repo to `~/dots` you can install it by running

```
cd ~/dots
rm -rf .git README.md screenshot.png
cp -rT . ~
```

**this will overwrite any previous config files you had, make sure to backup!** *(if you care for your own config files)*

otherwise, you can just copy any specific config you want
