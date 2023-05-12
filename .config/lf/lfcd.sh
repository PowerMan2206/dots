# you gotta source this for it to work
# makes it so that quitting lf drops you into the dir you were in in lf

lfcd () {
    tmp="$(mktemp)"
    \lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        dir="$(cat "$tmp")"
        \rm -f "$tmp"
        if [ -d "$dir" ]; then
            if [ "$dir" != "$(pwd)" ]; then
                cd "$dir"
            fi
        fi
    fi
}
