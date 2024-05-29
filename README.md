# EYECRYPT
![](https://github.com/espimyte/eyecrypt/blob/main/assets/eyecrypt-icon.png?raw=true)

A tool that visualizes encryption in images.

## Table of Contents
- [OVERVIEW](#OVERVIEW)
  - [Background](#Background)
  - [Synopsis](#Synopsis) 
- [INSTALLATION](#INSTALLATION)
- [USAGE](#USAGE)
  - [GUI](#GUI)
  - [CLI](#CLI)
- [SUPPORTED ALGORITHMS](#SUPPORTED-ALGORITHMS)
- [SUPPORTED FILE TYPES](#SUPPORTED-FILE-TYPES)
- [EXAMPLES](#EXAMPLES)
- [ADDITIONAL NOTES](#ADDITIONAL-NOTES)
  - [Compability](#Compability)
  - [Metadata](#Metadata)
  - [Image Usage](#Image-Usage)

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

The intention of this program is not only to expedite the process, but to introduce this effect to others who may not be as knowledgeable in modes of encryption, and allow others to experiment with images and encryption themselves.

I think the effect that this encryption method performs on images is very beautiful, and I want to share this beauty with others. I hope you can find it as fascinating and wonderful as I do.

While this ECB encryption method may be "faulty" and "insecure", perhaps it is true that flaws are what make us beautiful.

## INSTALLATION
Simply run `EYECRYPT.exe`! No external installations required.

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

If you wish to be able to call EYECRYPT from anywhere, you can add the folder that contains the `eyecrypt.exe` file to your `PATH`. If done successfuly, you should be able to run the program from anywhere using `eyecrypt`.

You may require a system restart after adding the program to the path before using it.

Usage Examples
```
$ eyecrypt -in "input.png" -out "output.png"
$ eyecrypt -in "png-image.png" -out "jpg-image.jpg"
$ eyecrypt -in "input.png" -out "output.jpg" -algo camellia-128-ecb
$ eyecrypt -in "input.png" -out "output.jpg" -algo cast5-ecb -key FFD1DC
$ eyecrypt -in "input.png" -out "output.jpg" -algo aria-128-cfb -iv 111 -key ffa
```
By default, EYECRYPT uses `aes-128-ecb`, with key `0x00000000000000000000000000000000`, and iv/nonce of `0x00000000000000000000000000000000` (if applicable).

## SUPPORTED ALGORITHMS

**ECB** = `aes-128-ecb, aes-192-ecb, aes-256-ecb, camellia-128-ecb, camellia-192-ecb, camellia-256-ecb, seed-ecb, sm4-ecb, cast5-ecb, bf-ecb, idea-ecb, des3-64-ecb`

**CBC** = `aes-128-cbc, aes-192-cbc, aes-256-cbc, camellia-128-cbc, camellia-192-cbc, camellia-256-cbc, seed-cbc, sm4-cbc, cast5-cbc, bf-cbc, idea-cbc, des-64-cbc`

**CTR** = `aes-128-ctr, aes-192-ctr, aes-256-ctr, camellia-128-ctr, camellia-192-ctr, camellia-256-ctr, sm4-ctr`

**OFB** = `aes-128-ofb, aes-192-ofb, aes-256-ofb, camellia-128-ofb, camellia-192-ofb, camellia-256-ofb, seed-ofb, sm4-ofb, cast5-ofb, bf-ofb, idea-ofb, des3-64-ofb`

**CFB** = `aes-128-cfb, aes-192-cfb, aes-256-cfb, camellia-128-cfb, camellia-192-cfb, camellia-256-cfb, seed-cfb, sm4-cfb, cast5-cfb, bf-cfb, idea-cfb, des3-64-cfb`

**OTHER** = `rc4-128`

## SUPPORTED FILE TYPES
- PNG `.png`
- JPG `.jpg`
- JPEG `.jpeg`
- BMP `.bmp`
- WEBP `.webp`
- APNG `.apng`

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
EYECRYPT stores the resulting algorithm, key, and iv/nonce (if applicable) in the EXIF of the output image.

There are a variety of tools online that allow you to view the EXIF data. 

If you have `ImageMagick` installed, you can call the following to view the EXIF data.
```
magick identify -format '%[EXIF:*]' "your-image.png"
```

Please note that there is no guarantee that this EXIF data is preserved if the image is modified in anyway. If you wish to store the parameters you used to encrypt an image, it is reccomended that you store it elsewhere yourself and do not rely on the EXIF data.

### Image Usage
You are welcome to freely use any of the images that you create using this program. No restrictions and no permission or attribution required, as long as you had rights to the original image.

