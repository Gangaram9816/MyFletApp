; MyFletApp Inno Setup Script

[Setup]
AppName=MyFletApp
AppVersion=1.0.0
AppPublisher=YourName
AppPublisherURL=https://github.com/Gangaram9816/MyFletApp
DefaultDirName={pf}\MyFletApp
DefaultGroupName=MyFletApp
UninstallDisplayIcon={app}\src.exe
Compression=lzma
SolidCompression=yes
OutputDir=build  ; ✅ Ensure the installer is placed in the "build" folder
OutputBaseFilename=MyFletApp_Installer  ; ✅ Name of the output installer file
SetupIconFile=build\app.ico  ; ✅ Custom icon for the installer (optional)
ArchitecturesInstallIn64BitMode=x64  ; ✅ Force 64-bit installation mode
DisableDirPage=no  ; ✅ Allow user to choose installation directory

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "build\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\MyFletApp"; Filename: "{app}\src.exe"; IconFilename: "{app}\app.ico"
Name: "{commondesktop}\MyFletApp"; Filename: "{app}\src.exe"; IconFilename: "{app}\app.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional tasks:"

[Run]
Filename: "{app}\src.exe"; Description: "Launch MyFletApp"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

