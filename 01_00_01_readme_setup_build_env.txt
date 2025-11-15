Tested under windows 10 Home

1. Need to have Visual Studio 2015 installed ( e.g. VS 2015 Community Update 3, file name: vs2015.3.com_enu.iso )

2. Some parts can refer to https://github.com/mumble-voip/mumble-releng/blob/master/buildenv/1.3.x/win32-static/README

3. Some parts Can follow the BuildingWindows_Mumble_Wiki.pdf

4. Some download path and hash values are updated, can refer to https://github.com/ganjingdemo/mumble-releng/tree/master/buildenv/1.3.x/win32-static
The reposiotry is in https://github.com/ganjingdemo/mumble-releng.git.

5. Windows 10 SDK can use this one: 17763.132.181022-1834.rs5_release_svc_prod1_WindowsSDK
(The newest one may not work with VS2015).

https://developer.microsoft.com/en-us/windows/downloads/sdk-archive/index-legacy
https://go.microsoft.com/fwlink/p/?LinkID=2033686

17763.132.181022-1834.rs5_release_svc_prod1_WindowsSDK.iso
SHA256: 016981259708e1afcab666c7c1ff44d1c4d63b5e778af8bc41b4f6db3d27961a


6. During building, if cannot download the dependency, can search google and manually download. 

Or refer to the URL inside the build files in https://github.com/ganjingdemo/mumble-releng/tree/master/buildenv/1.3.x/win32-static then download manually.

Some source files can be found from https://github.com/ganjingdemo/mumble-releng-lib/tree/main/mumble_1_3_4_win

Put the downloaded file to build folder. 
e.g. 
C:\MumbleBuild\win64-static-1.3.x-2021-02-10-da6c376-926.build
or
C:\MumbleBuild\win32-static-1.3.x-2025-11-10-56f254d-928.build

Then run build-all.bash
e.g.
C:\github\ganjingdemo\mumble-releng\buildenv\1.3.x\win32-static\build-all.bash

If build failed in the middle, Can copy 

C:\github\ganjingdemo\mumble-releng\buildenv\1.3.x\win32-static\build-all.bash

to

C:\github\ganjingdemo\mumble-releng\buildenv\1.3.x\win32-static\build-all-partial.bash

and remove the already finished line then continue build.
