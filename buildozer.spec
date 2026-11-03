[app]

title = Agricultural Bank Services

package.name = agriculturalbank
package.domain = org.adelomar

source.dir = .
source.main = main.py

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,SEND_SMS

android.api = 35
android.minapi = 21

android.archs = arm64-v8a,armeabi-v7a

source.include_exts = py,png,jpg,jpeg,kv,json
source.exclude_exts = pyc,pyo

android.private_storage = True
android.accept_sdk_license = True

log_level = 2


[buildozer]

build_dir = .buildozer
bin_dir = bin
log_level = 2
