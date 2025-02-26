
[Setup]
AppName=MyFletApp
AppVersion=1.0.0
DefaultDirName={autopf}\MyFletApp
DefaultGroupName=MyFletApp
OutputDir=.
OutputBaseFilename=MyFletApp_Installer
Compression=lzma2
SolidCompression=yes
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\src.exe
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "build\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\MyFletApp"; Filename: "{app}\src.exe"

[Run]
Filename: "{app}\src.exe"; Description: "Launch MyFletApp"; Flags: nowait postinstall skipifsilent