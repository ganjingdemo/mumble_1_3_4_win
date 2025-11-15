How to build Mumble 1.3.4 windows static binary (64 bit)

Tested under windows 10 Home

Need to have Visual Studio 2015 installed ( e.g. VS 2015 Community Update 3, file name: vs2015.3.com_enu.iso )

Some parts can refer to https://github.com/mumble-voip/mumble-releng/blob/master/buildenv/1.3.x/win32-static/README

1. Start a cygwin console.

(1) Method 1
cd /d C:\MumbleBuild\win64-static-1.3.x-2021-02-10-da6c376-926
prep.cmd
cygwin.cmd

(2) Method 2
Run "C:\MumbleBuild\win64-static-1.3.x-2021-02-10-da6c376-926\MumbleBuild - cygwin.lnk"

The content of the lnk: "%WINDIR%\system32\cmd.exe /k prep.cmd && cygwin.cmd"

start in "C:\MumbleBuild\win64-static-1.3.x-2021-02-10-da6c376-926"


2. Get source code

Assume you already create folder c:\dev

$ cd /cygdrive/c/dev

$ pwd
/cygdrive/c/dev

git clone https://github.com/ganjingdemo/mumble_1_3_4_win.git mumble


3. Build and make installer

cd /cygdrive/c/dev/mumble

(1) Optional (assume python3 is installed in the build machine):

If you want to change the build version, can update update_version.py then run 

python update_version.py

(2) Then call the following batch files:

. set_64_bit_rc_path.bash
# To add "/cygdrive/c/Program Files (x86)/Windows Kits/10/bin/10.0.17763.0/x64" to path

./01_01_generate_makefile.bat
./02_update_makefile.bat
./03_compile_mumble.bat

After build, the binary is under the release folder.

(3) Make installer

Need to install wix 3.x (https://github.com/wixtoolset/wix3/releases/download/wix3141rtm/wix314.exe)

[1] Start a VS2015 command line console from

"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2015\Visual Studio Tools\Windows Desktop Command Prompts\VS2015 x64 Native Tools Command Prompt.lnk"

or run

cd /d "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\"
vcvarsall.bat amd64

[2] cd /d c:\dev\mumble

[3] 06_build_installer_64bit.bat