# EYECRYPT
A tool that visualizes encryption in images.

## Table of Contents
- [OVERVIEW](#OVERVIEW)
- [INSTALLATION](#INSTALLATION)
  - [Verifying your installation](#Verifying-your-installation)
- [USAGE](#USAGE)
- [IMAGE LICENSE](#IMAGE-LICENSE)

## INSTALLATION
This program requires both [ImageMagick](https://imagemagick.org/script/download.php) and [OpenSSL](https://wiki.openssl.org/index.php/Binaries) to be installed on your device to function.

They can be downloaded from the links above. Follow the corresponding instructions to install the program.

### Verifying your installation
To check if ImageMagick is properly installed for this program, type the following into any terminal:
```
magick -version
```
If you see version information about ImageMagick, the program is properly installed.
<br></br>
To check if OpenSSL is properly installed for this program, type the following into any terminal:
```
openssl version
```
If you see version information about OpenSSL, the program is properly installed.

## USAGE
Two versions of EYECRYPT are provided, a GUI version, and a CLI version.

### GUI

The GUI version can be considered the "main" and reccomended version of EYECRYPT. It is intended to be user friendly and not require the user to fiddle with the command line.

### CLI

The CLI version is a version designed for the command line. This is an option provided for users that for any reason would require/prefer the ability to use EYECRYPT in the command line.

The CLI version of EYECRYPT can simply be ran by calling the path to the `eyecrypt.exe` file from the command line.

If you wish to be able to call EYECRYPT from anywhere, you can add the folder that contains the `eyecrypt.exe` file to your PATH, and if done successfuly, you should be able to run the program from anywhere using `eyecrypt`.

You may require a system restart after adding the program to the path before using it.

## IMAGE LICENSE
While I reserve rights to the program itself, I reserve no rights to any images produced by this program. 
You are welcome to use any images produced by this program freely for any projects, personal or commercial, no attribution or permission required.
