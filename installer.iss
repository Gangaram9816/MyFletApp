[Setup]
AppName=MyFletApp
AppVersion=1.0.0
AppPublisher=YourName
AppPublisherURL=https://github.com/Gangaram9816/MyFletApp
DefaultDirName={pf}\MyFletApp
DefaultGroupName=MyFletApp
UninstallDisplayIcon={app}\MyFletApp.exe
Compression=lzma
SolidCompression=yes
OutputDir=build
OutputBaseFilename=MyFletApp_Installer
SetupIconFile=build\app.ico
ArchitecturesInstallIn64BitMode=x64
DisableDirPage=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "build\MyFletApp_{#AppVersion}.exe"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\MyFletApp"; Filename: "{app}\MyFletApp.exe"; IconFilename: "{app}\app.ico"
Name: "{commondesktop}\MyFletApp"; Filename: "{app}\MyFletApp.exe"; IconFilename: "{app}\app.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional tasks:"

[Run]
Filename: "{app}\MyFletApp.exe"; Description: "Launch MyFletApp"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
