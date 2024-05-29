# EYECRYPT
![](https://github.com/espimyte/eyecrypt/blob/main/assets/eyecrypt-icon.png?raw=true)

A tool that visualizes encryption in images.

## Table of Contents
- [OVERVIEW](#OVERVIEW)
  - [Background](#Background)
  - [Synopsis](#Synopsis) 
- [INSTALLATION](#INSTALLATION)
  - [Verifying your installation](#Verifying-your-installation)
- [USAGE](#USAGE)
  - [GUI](#GUI)
  - [CLI](#CLI)
- [SUPPORTED ALGORITHMS](#SUPPORTED-ALGORITHMS)
- [SUPPORTED FILE TYPES](#SUPPORTED-FILE-TYPES)
- [EXAMPLES](#EXAMPLES)
- [ADDITIONAL NOTES](#ADDITIONAL-NOTES)
  - [Compability](#Compability)
  - [Metadata](#Metadata) 
- [IMAGE LICENSE](#IMAGE-LICENSE)

## OVERVIEW

### Background
EYECRYPT is a program that is inspired by the following image, which I found on the [wikipedia page on block cipher encryption](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation) in 2021, demonstrating how ECB encryption fails to properly obfuscate data, in contrast to other encryption methods.

![](https://i.imgur.com/Z896Mym.png)

I thought that the effect produced by the faulty encryption method was fascinating, and so I sought out to find a way to do it myself.

When images are encrypted, they cannot be read as images anymore. So something must be done to the image after it is encrypted in order for it to be read as an image.

After some research, I was able to learn about how this effect is achieved, and I managed to successfully reproduce the effect myself.

You can learn more yourself [here](https://words.filippo.io/the-ecb-penguin/) and [here](https://samsclass.info/seminars/image-ECB.html).

Below is an image that I created to help me remember the process.

![](https://github.com/espimyte/eyecrypt/blob/main/assets/process.png?raw=true)

Of course, I was estatic about the result. I wanted to see more! 

Unfortunately, performing this process for each image was rather tedious and I was very lazy. So, I sought a tool online that could perform this for me, to no success.

In addition, there was the issue of different file types. Injecting a BMP header will not work for images that are not BMP. That means either injecting a different header for each image type, or converting each image to BMP. 

Another process that, while simple, can add up to be very tedious over several images.

And so...

### Synopsis

EYECRYPT is a tool I created to expedite the process of visualizing encryption on images! 

The program supports several image types in addition to BMP, including the most commonly used such as PNG and JPG.

It also has a feature that allows one to randomize a key, allowing one to quickly experiment with how the key changes the result. 

An image can be encrypted and visualized quickly, without having to convert the images manually, or poke around with the bytes of a file. 

EYECRYPT also supports almost all of the cipher methods that OpenSSL offers, from ECB to CBC, and more!

The intention of this program is not only to expedite the process, but to introduce this effect to others who may not be as knowledgeable in modes of encryption, and allow others to experiment with images and encryption themselves.

I think the effect that this encryption method performs on images is very beautiful, and I want to share this beauty with others. I hope you can find it as fascinating and wonderful as I do.

While this ECB encryption method may be "faulty" and "insecure", perhaps it is true that flaws are what make us beautiful.

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

After ImageMagick and OpenSSL are installed, you can run `EYECRYPT.exe`!

## USAGE
Two versions of EYECRYPT are provided, a GUI version, and a CLI version.

### GUI
<img src="https://github.com/espimyte/eyecrypt/blob/main/assets/eyecrypt-icon.png?raw=true" style="width: 50px; image-rendering: pixelated"></img>

The GUI (graphical user interface) version can be considered the "main" and reccomended version of EYECRYPT.

It is intended to be user friendly and not require the user to fiddle with the command line.

![](https://github.com/espimyte/eyecrypt/blob/main/assets/eyecrypt-demo.gif?raw=true)

> [!IMPORTANT]  
> It is reccomended to use smaller, high contrast images if you wish to see more discernable results. Photos, large images, and/or images with a lot of noise tend to produce more obfuscated results.

### CLI
<img src="https://github.com/espimyte/eyecrypt/blob/main/assets/eyecrypt-cli-icon.png?raw=true" style="width: 50px; image-rendering: pixelated"></img>

The CLI (command line interface) version is a version designed for the command line. 

This is an option provided for users that for any reason would require/prefer the ability to use EYECRYPT in the command line.

The CLI version of EYECRYPT can simply be ran by calling the path to the `eyecrypt.exe` file from the command line.

If you wish to be able to call EYECRYPT from anywhere, you can add the folder that contains the `eyecrypt.exe` file to your `PATH`, and if done successfuly, you should be able to run the program from anywhere using `eyecrypt`.

You may require a system restart after adding the program to the path before using it.

Usage Examples
```
$ eyecrypt -in "input.png" -out "output.png"
$ eyecrypt -in "png-image.png" -out "jpg-image.jpg"
$ eyecrypt -in "input.png" -out "output.jpg" -algo camellia-128-ecb
$ eyecrypt -in "input.png" -out "output.jpg" -algo cast5-ecb -key FFD1DC
$ eyecrypt -in "input.png" -out "output.jpg" -algo aria-128-cfb -iv 111 -key ffa
```
By default, EYECRYPT uses `aes-128-ecb`, with key `0x00000000000000000000000000000000`, and an IV (initialization value) of `0` (if applicable).

With the CLI, you will not be stopped when trying to use unsupported algorithms or file types. I cannot guarantee that will work, though I will not stop you from trying!

## SUPPORTED ALGORITHMS

**ECB** = aes-128-ecb, aes-192-ecb, aes-256-ecb, aria-128-ecb, aria-192-ecb, aria-256-ecb, bf-ecb, camellia-128-ecb, camellia-192-ecb, camellia-256-ecb, cast5-ecb, des-ecb, idea-ecb, rc2-ecb, rc5-ecb, seed-ecb, sm4-ecb

**CBC** = aes-128-cbc, aes-192-cbc, aes-256-cbc, aria-128-cbc, aria-192-cbc, aria-256-cbc, bf-cbc, camellia-128-cbc, camellia-192-cbc, camellia-256-cbc, cast-cbc, cast5-cbc, des-cbc, des-ede-cbc, des-ede3-cbc, idea-cbc, rc2-40-cbc, rc2-64-cbc, rc2-cbc, rc5-cbc, seed-cbc, sm4-cbc

**CFB** = aria-128-cfb, aria-128-cfb1, aria-128-cfb8, aria-192-cfb, aria-192-cfb1, aria-256-cfb8, bf-cfb, cast5-cfb, des-cfb, des-ede-cfb, des-ede3-cfb, idea-cfb, rc2-cfb, rc5-cfb, seed-cfb, sm4-cfb

**CTR** = aria-128-ctr, aria-192-ctr, aria-256-ctr, sm4-ctr

**OFB** = aria-128-ofb, aria-192-ofb, aria-256-ofb, bf-ofb, cast5-ofb, des-ede-ofb, des-ofb, idea-ofb, rc2-ofb, rc5-ofb, seed-ofb, sm4-ofb

**OTHER** = base64, bf, cast, des, des-ede, des-ede3, des3, desx, idea, rc2, rc4, rc4-40, rc5, seed

> [!NOTE]  
> Some algorithms which are considered "legacy" may not work (for example, algorithms containing 'des'), depending on your machine.

## SUPPORTED FILE TYPES
- PNG (.png)
- JPG (.jpg)
- JPEG (.jpeg)
- BMP (.bmp)
- BMP (.bmp)
- GIF (.gif)
- WEBP (.webp)
- APNG (.apng)

Note that while animated images (such as .gif) are accepted, they will not preserve their animation after the process.

## EXAMPLES

| Original Image  | Result | Parameters |
| ------------- | ------------- | ------------- |
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/example.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/example-result10.png?raw=true)   | **Algorithm:**<br>aes-128-ecb<br><br>**Key:**<br>7c221e585bcfba398c303b59ebc29331<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/example.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/example-result5.png?raw=true)   | **Algorithm:**<br>des-ede<br><br>**Key:**<br>49c94498ada5a0b04f926d8aa76da972<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/rearranger.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/rearranger-result.png?raw=true)   | **Algorithm:**<br> camellia-128-ecb<br><br>**Key:**<br>4ce44843bb9db8ae671708125435628f<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/vacuum.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/vacuum-result.png?raw=true)   | **Algorithm:**<br> des-ede<br><br>**Key:**<br>3299d0c42940bd851c7ab03f3e7f7637<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/izzy.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/izzy-result.png?raw=true)   | **Algorithm:**<br>aria-256-ecb<br><br>**Key:**<br> ff9ecd0e5a3865c4df8c40afef0bfbc1<br>|


## ADDITIONAL NOTES

### Compability
This program has only been tested on Windows. I cannot guarantee that it works on other operating systems.

### Metadata
EYECRYPT stores the resulting algorithm, key, and iv (if applicable) in the metadata of the output image.

To view this metadata, type the following into the terminal:
```
magick identify -format %c "your-image.png"
```
Please note that there is no guarantee that this metadata is preserved if the image is modified in anyway. If you wish to store the parameters you used to encrypt an image, it is reccomended that you store it elsewhere yourself and do not rely on the metadata.

## IMAGE RIGHTS
I reserve no rights to any images produced by this program. 
You are welcome to use any images produced by this program freely for any projects, personal or commercial, no attribution or permission required.
