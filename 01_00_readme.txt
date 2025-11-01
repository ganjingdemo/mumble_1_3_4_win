How to build Mumble 1.3.4 windows static binary

Some parts can refer to https://github.com/mumble-voip/mumble-releng/blob/master/buildenv/1.3.x/win32-static/README

1. Start a cygwin console.

(1) Method 1
cd /d C:\MumbleBuild\win32-static-1.3.x-2020-10-05-e590ac8-925
prep.cmd
cygwin.cmd

(2) Method 2
Run "C:\MumbleBuild\win32-static-1.3.x-2020-10-05-e590ac8-925\MumbleBuild - cygwin.lnk"

The content of the lnk: "%WINDIR%\system32\cmd.exe /k prep.cmd && cygwin.cmd"

start in "C:\MumbleBuild\win32-static-1.3.x-2020-10-05-e590ac8-925"

2.
$ cd /cygdrive/c/MumbleBuild/

$ pwd
/cygdrive/c/MumbleBuild

git clone https://github.com/ganjingdemo/mumble_1_3_4_win.git

3.
cd /cygdrive/c/MumbleBuild/mumble_1_3_4_win

Then call the following batch files ( assume you don't want to build server program ):

./01_02_generate_makefile_no_server.bat
./02_update_makefile.bat
./03_compile_mumble.bat

After build, the binary is under the release folder.

See the following file list:

$ pwd
/cygdrive/c/MumbleBuild/mumble_1_3_4_win/release

$ ls *.exe
mumble.exe  mumble_ol_helper.exe  mumble_ol_helper_x64.exe

$ ls *.dll
celt0.0.11.0.dll  celt0.0.7.0.dll  mumble_app.dll  mumble_ol.dll  mumble_ol_x64.dll  opus.dll  rnnoise.dll  speex.dll