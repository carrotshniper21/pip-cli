#!/bin/bash

display_help() {
    echo '''Usage: [option...] [-h] [-d]
            -h, --help              Display this message and exit
            -d, --download          Download the selected media'''

    exit 1
}

while :
do
    case "$1" in
      -h | --help)
          display_help
          exit 0
          ;;

      -d | --download)
          echo "Downloading..."
          shift
          ;;

      --) # End of all options
          shift
          break
          ;;
      -*)
          echo "Error: Unknown option: $1" >&2
          exit 1
          ;;
      *)  # No more options
          break
          ;;
    esac
done

