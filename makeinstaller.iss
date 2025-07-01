; http://www.jrsoftware.org/ishelp/index.php

[Setup]
AppName="Python Audio Analysis Music Player "
AppVerName="Python Audio Analysis Music Player  1.1.0"
DefaultDirName="{pf}\PyMusicPlayer"
DefaultGroupName="Python Audio Analysis Music Player "
AppVersion="1.1.0"
AppCopyright="Ankit Singh"
AppPublisher="Ankit Singh"
UninstallDisplayIcon="{app}\PyMusicPlayer.exe"
Compression=lzma2/max
SolidCompression=yes
OutputDir="dist"
OutputBaseFilename="PyMusicPlayer-1.1.0-Setup"
; VersionInfoVersion="1.1.0"
VersionInfoProductVersion="1.1.0"
VersionInfoCompany="Ankit singh"
VersionInfoCopyright="Ankit Singh"
ArchitecturesInstallIn64BitMode="x64"

[Files]
Source: "dist\PyMusicPlayer\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\PyMusicPlayer"; Filename: "{app}\PyMusicPlayer.exe"
Name: "{commondesktop}\PyMusicPlayer"; Filename: "{app}\PyMusicPlayer.exe"
