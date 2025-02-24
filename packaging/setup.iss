[Setup]
AppName=Flet App
AppVersion=1.0.0
DefaultDirName={pf}\FletApp
OutputBaseFilename=FletAppInstaller
Compression=lzma2
SolidCompression=yes

[Files]
Source: "build\FletApp.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "src\updater.py"; DestDir: "{app}"

[Icons]
Name: "{group}\Flet App"; Filename: "{app}\FletApp.exe"

[Run]
Filename: "{app}\updater.py"; Parameters: "/silent"; Flags: nowait postinstall
