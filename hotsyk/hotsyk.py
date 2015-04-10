# -*- coding: utf-8 -*-
import webbrowser


def cv(open_browser=False):
    """Return url to CV"""
    link = "http://hotsyk.com/cv/"
    if open_browser:
        return webbrowser.open_new_tab(link)
    return link


def talks(open_browser=False):
    """Return url to page with list of talk"""
    link = "http://hotsyk.com/talks/"
    if open_browser:
        return webbrowser.open_new_tab(link)
    return link
