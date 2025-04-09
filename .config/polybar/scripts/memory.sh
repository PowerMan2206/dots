#!/bin/bash
# hacky way to get the "GiB" is only displayed once at the end

memory="$(free -m | grep Mem | tr -s ' ')"

total_raw="$(echo $memory | cut -d' ' -f2)"
 used_raw="$(echo $memory | cut -d' ' -f3)"

total="$(calc "round(${total_raw} / 1000,2)" | xargs)"
 used="$(calc "round(${used_raw}  / 1000,2)" | xargs)"

# wonky way to have trailing zeroes for a cleaner look
# ex.  3.9 --> 3.90
useddot="$(echo $used | grep -o "\..*$")"
case ${#useddot} in
	0 ) used=${used}.00 ;;
	2 ) used=${used}0   ;;
esac

echo "${used}/${total} GB"
