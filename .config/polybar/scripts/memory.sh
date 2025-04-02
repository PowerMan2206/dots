#!/bin/bash
# hacky way to get the "GiB" is only displayed once at the end

memory="$(free -m | grep Mem | tr -s ' ')"

total_raw="$(echo $memory | cut -d' ' -f2)"
 used_raw="$(echo $memory | cut -d' ' -f3)"

total="$(calc "round(${total_raw} / 1000,2)" | xargs)"
 used="$(calc "round(${used_raw}  / 1000,2)" | xargs)"

echo "${used}/${total} GB"
