#Original Respository: https://github.com/rockofox/predator

if [ "$#" != 0 ]; then
        cd "$@"
        return
fi
while true; do
        lsd=$(echo ".." && ls -p) # | grep '/$' | sed 's;/$;;')
        dir="$(printf '%s\n' "${lsd[@]}" |
                fzf --reverse --preview '
                        __cd_nxt="$(echo {})";
                        __cd_path="$(echo $(pwd)/${__cd_nxt} | sed "s;//;/;")";
                        echo $__cd_path;
                        echo;
                        if [ "${__cd_path: -1}" = "/" ] || [ "${__cd_path}" = "$(pwd)/.." ];
                        then
                                ls -p --color=always "${__cd_path}"
                        else
                                __ext="${__cd_path: -4}"
                                case "${__ext}" in
                                        ".jpg" | ".png" | ".gif")
                                                chafa -w 1 "${__cd_path}"
                                                ;;
                                        *)
                                                if [ $(command -v bat) ];
                                                then
                                                        bat "${__cd_path}" --color=always;
                                                else
                                                        ${PAGER:-less} "${__cd_path}"
                                                fi
                                                ;;
                                esac
                        fi
                        ')"
        if [ ${#dir} = 0 ]; then
                break
        fi
        if [ "${dir: -1}" = "/" ] || [ "${dir}" = ".." ]; then
                cd "$dir" &>/dev/null
        else
                ext="${dir: -4}"
                case "$ext" in
                ".jpg" | ".png" | ".gif")
                        feh "$dir"
                        ;;
                *)
                        if [ $(file -b --mime-type "$dir" | sed 's|/.*||') = "text" ]; then
                                printf "%s/%s\n" "$(pwd)" "$dir"
                                exit 0
                        else
                                xdg-open "$dir"
                        fi
                        ;;
                esac

        fi
done

