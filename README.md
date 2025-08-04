# Fusion ScreenShotter
A lightweight command utility that allows for assigning a key command to "Capture Image..."

## Overview
This is just a small python add-in that enables calling "Capture Image..." from a key command. This command is typically found in the File menu and has no key command by default.

## Installation

1. Download or clone this repository
2. Copy the entire `ScreenShotter` folder to your Fusion 360 add-ins directory:
   - **Windows**: `%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns\`
   - **macOS**: `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/`
3. Start Fusion 360
4. Go to **Tools** > **Scripts and Add-Ins**
5. Select the **Add-Ins** tab
6. Find "ScreenShotter" in the list
7. Select it and click **Run**
8. Check "Run on Startup" if you want it to load automatically
9. The add-in icon will apear in the Utilities > Add-ins toolbar and can be assigned a key command (I typically use "cmd/ctrl-shift-e")
