[Setup]
AppName=MyFletApp
AppVersion=1.0.0
DefaultDirName={autopf}\MyFletApp
DefaultGroupName=MyFletApp
OutputBaseFilename=MyFletApp_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "build\src.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\*.*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\MyFletApp"; Filename: "{app}\src.exe"

[Run]
Filename: "{app}\src.exe"; Description: "Launch MyFletApp"; Flags: nowait postinstall skipifsilent
