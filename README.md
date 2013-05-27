chartmix
========

Creates a Grooveshark-able mix of music from the current charts

Install Instructions
====================
1) Request a tinysong.com api key and export it as an env var (TINYSONG_KEY) before running the chartmix script.
    export TINYSONG_KEY=abc123
2) Download and install simplejson
3) Download and install feedparser

Run Instructions
================
4) Run the script as follows:
    python chartmix.py
5) Go to Grooveshark.com and let the page load. At this point, the window object will be available to you, along with a "Grooveshark" object. Paste the output from chartmix in the address bar and hit enter.
    javascript: window.Grooveshark.addSongsByID([ song1, song2, etc. ])
Wait a moment and the songs should be added to Now Playing.

That's it!
