#!/bin/bash
# hacky way to get the "GiB" is only displayed once at the end

memory="$(free -m --si | grep Mem)"

total_raw="$(echo $memory | cut -d' ' -f2)"
 used_raw="$(echo $memory | cut -d' ' -f3)"

# divide by 1000 to get GB from MB
# end zero hardcoded because the total doesn't change
total="$(calc "round(${total_raw} / 1000,2)" | xargs)0"
 used="$(calc "round(${used_raw}  / 1000,2)" | xargs)"

# wonky way to have trailing zeroes for a cleaner look
# ex.  3.9 --> 3.90, 2 --> 2.00
useddot="$(echo $used | grep -o "\..*$")" # number of characters after (and including) the dot
case ${#useddot} in
	0 ) used=${used}.00 ;;
	2 ) used=${used}0   ;;
esac

echo "${used}/${total} GB"
