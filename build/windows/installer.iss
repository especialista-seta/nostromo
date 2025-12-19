; NOSTROMO Windows Installer
; Built with Inno Setup (https://jrsoftware.org/isinfo.php)
;
; To build: iscc build/windows/installer.iss

#define MyAppName "NOSTROMO"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "NOSTROMO Project"
#define MyAppURL "https://github.com/especialista-seta/nostromo"
#define MyAppExeName "nostromo.exe"
#define MyAppDescription "MU-TH-UR 6000 AI Interface"

[Setup]
; Application info
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}/issues
AppUpdatesURL={#MyAppURL}/releases
AppComments={#MyAppDescription}

; Installation paths
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes

; Output settings
OutputDir=..\..\dist\installer
OutputBaseFilename=nostromo-{#MyAppVersion}-windows-setup
SetupIconFile=nostromo.ico

; Compression
Compression=lzma2/ultra64
SolidCompression=yes
LZMAUseSeparateProcess=yes

; Privileges (don't require admin unless installing for all users)
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog

; Modern installer appearance
WizardStyle=modern
WizardImageFile=wizard.bmp
WizardSmallImageFile=wizard-small.bmp

; Version info
VersionInfoVersion={#MyAppVersion}
VersionInfoCompany={#MyAppPublisher}
VersionInfoDescription={#MyAppDescription}
VersionInfoTextVersion={#MyAppVersion}
VersionInfoCopyright=Copyright (c) 2024 {#MyAppPublisher}
VersionInfoProductName={#MyAppName}
VersionInfoProductVersion={#MyAppVersion}

; Uninstaller
UninstallDisplayIcon={app}\{#MyAppExeName}
UninstallDisplayName={#MyAppName}

; Allow user to select install type
AllowNoIcons=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Types]
Name: "full"; Description: "Full installation (recommended)"
Name: "compact"; Description: "Compact installation"
Name: "custom"; Description: "Custom installation"; Flags: iscustom

[Components]
Name: "main"; Description: "NOSTROMO Core Application"; Types: full compact custom; Flags: fixed
Name: "shortcuts"; Description: "Desktop and Start Menu shortcuts"; Types: full
Name: "path"; Description: "Add to system PATH"; Types: full

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Components: shortcuts
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Components: shortcuts; Flags: unchecked
Name: "addtopath"; Description: "Add NOSTROMO to system PATH"; GroupDescription: "System Integration:"; Components: path

[Files]
; Main application files (from PyInstaller output)
Source: "..\..\dist\nostromo\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Components: main

[Icons]
; Start Menu
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Comment: "{#MyAppDescription}"
Name: "{group}\{#MyAppName} Documentation"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

; Desktop
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon; Comment: "{#MyAppDescription}"

; Quick Launch
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Registry]
; Add to PATH (user-level)
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Tasks: addtopath; Check: NeedsAddPath('{app}')

[Run]
; Option to launch after install
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Parameters: "status"; Flags: nowait postinstall skipifsilent shellexec

[UninstallRun]
; Nothing special needed

[UninstallDelete]
; Clean up config on uninstall (optional - uncomment to enable)
; Type: filesandordirs; Name: "{userappdata}\nostromo"

[Code]
// Check if directory is already in PATH
function NeedsAddPath(Param: string): boolean;
var
  OrigPath: string;
begin
  if not RegQueryStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', OrigPath) then
  begin
    Result := True;
    exit;
  end;
  // Look for the path with leading and trailing semicolon
  Result := Pos(';' + Param + ';', ';' + OrigPath + ';') = 0;
end;

// Remove from PATH on uninstall
procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
var
  Path: string;
  AppPath: string;
  P: Integer;
begin
  if CurUninstallStep = usPostUninstall then
  begin
    if RegQueryStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', Path) then
    begin
      AppPath := ExpandConstant('{app}');
      P := Pos(';' + AppPath, Path);
      if P > 0 then
      begin
        Delete(Path, P, Length(';' + AppPath));
        RegWriteStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', Path);
      end
      else
      begin
        P := Pos(AppPath + ';', Path);
        if P > 0 then
        begin
          Delete(Path, P, Length(AppPath + ';'));
          RegWriteStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', Path);
        end;
      end;
    end;
  end;
end;

// Custom welcome message
function InitializeSetup(): Boolean;
begin
  Result := True;
end;

procedure InitializeWizard();
begin
  WizardForm.WelcomeLabel2.Caption := 
    'This will install {#MyAppName} {#MyAppVersion} on your computer.' + #13#10 + #13#10 +
    'NOSTROMO is an AI-powered terminal interface featuring MU-TH-UR 6000, ' +
    'the iconic computer from the USCSS Nostromo.' + #13#10 + #13#10 +
    'Click Next to continue, or Cancel to exit Setup.';
end;
