#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logo
import movie
import util

def main():
    # TODO: put the logo back
    print(logo.display_prettier_logo())
    prefix = "https://vipstream.tv"

    if util.internet_working():
        movie.init_movie_protocol(prefix)


if __name__ == '__main__':
    main()












