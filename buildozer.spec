[app]
title = Tahadi
package.name = tahadi
package.domain = org.sulaiman
source.main = main.py
source.dir = .
version = 1.0
requirements = python3,kivy,arabic_reshaper,python-bidi
android.archs = arm64-v8a
orientation = portrait
fullscreen = 1
source.include_exts = py,ttf,png,jpg,kv,atlas,ogg,mp3,wav
source.include_patterns = assets/*
presplash.filename = assets/presplash.png
icon.filename = assets/icon.png
android.minapi = 21
android.use_sdl2 = 1

[buildozer]
log_level = 2
warn_on_root = 1
