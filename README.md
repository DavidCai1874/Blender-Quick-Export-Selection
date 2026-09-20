# Blender Quick Export Selection

Open the export window for selected objects with a single click.

## The Problem It Solves

Blender's "Selected Only" export option isn't enabled by default. It's easy to forget to check it and accidentally export your entire 1 GB scene. This add-on opens Blender's native export window with "Selected Only" already enabled.

![Screenshot 1](Readme_Images/1.png)

![Screenshot 2](Readme_Images/2.png)

## Installation

Requires Blender 4.5 or newer.

1. Download [`quick_export_selection-0.1.0.zip`](dist/quick_export_selection-0.1.0.zip) from the `dist` folder. Do not extract it.
2. In Blender, open **Edit > Preferences > Add-ons**.

   ![Add-ons preferences](Readme_Images/3.png)

3. Open the menu in the upper-right corner, choose **Install from Disk**, and select the ZIP file.

   ![Install from Disk](Readme_Images/4.png)

4. Enable the extension if it is not enabled automatically.
5. Enjoy!

   ![Quick Export Selection](Readme_Images/5.png)

## How It Works

Opens Blender's native export window with the selection-only option set to `True`.

## Planned Support

Support for additional formats, including USD and glTF, is planned.
