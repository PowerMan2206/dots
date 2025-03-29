# dots
Everyone must have a dotfiles repo, right?

![screenshot](https://raw.githubusercontent.com/PowerMan2206/dots/master/screenshot.png)

**STILL IN PROCESS OF MIGRATION:** I used to run i3, then switched to Sway, now I'm back on i3. It might take a bit to get everything back in place (and better)

## Packages and stuff

package       | why
--------------|--------------
`i3`          | window manager
`picom`       | compositor
`alacritty`   | terminal
`firefox`     | browser
`pipewire`    | audio stuff
`dmenu`       | launcher
`polybar`     | bar
`redshift`    | no eye hurty thing
`mpd/ncmpcpp` | music playback
`fastfetch`   | system info

Others are in `.config/packagelist`, install them with `paru -S - < packagelist` (or whatever AUR helper you have)

Colors are a mix of [srcery](https://srcery.sh) and [Sweet](https://github.com/EliverLara/Sweet)

## Installation

You can treat this repo as your home directory, so if you cloned the repo to `~/dots` you can install it by running

```
cd ~/dots
rm -rf .git README.md screenshot.png
cp -rT . ~
```

***THIS WILL OVERWRITE ANY CONFIG FILES YOU HAVE!***

Otherwise, you can just copy any specific config you want
