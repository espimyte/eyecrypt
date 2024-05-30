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
    - [Usage Examples](#Usage-Examples) 
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

And so...

### Synopsis

EYECRYPT is a tool I created to visualize encryption on images! 

- The program supports several image types in addition to BMP (including the most commonly used such as PNG and JPG) and a variety of encryption algorithms.
- It also has a feature that allows one to randomize a key (a value used for encrypting and decrypting an image), allowing one to quickly experiment with how changing the key changes the result.
- With the inclusion of other encryption algorithms, you can also experiment with how changing the encryption algorithm changes the result as well.
- Try experimenting with different key and algorithm combinations!

An image can be encrypted and visualized quickly, without having to convert the images manually, or poke around with the bytes of a file. 

The intention of this program is not only to expedite the process, but to introduce this effect to others who may not be as knowledgeable in modes of encryption, and allow others to experiment with images and encryption themselves.

I think the effect that these encryption methods perform on images is very beautiful, and I want to share this beauty with others. I hope you can find it as fascinating and wonderful as I do.

While this ECB encryption method may be "faulty" and "insecure", perhaps it is true that flaws are what make us beautiful.

## INSTALLATION
Simply run `EYECRYPT.exe`! No external installations required.

## USAGE
Two versions of EYECRYPT are provided, a GUI version, and a CLI version.

### GUI
<img src="https://github.com/espimyte/eyecrypt/blob/main/assets/eyecrypt-icon.png?raw=true" style="width: 50px; image-rendering: pixelated"></img>

The GUI (graphical user interface) version can be considered the "main" and reccomended version of EYECRYPT.

It is intended to be user friendly and not require the user to fiddle with the command line.

To use it, simply run the provided `EYECRYPT.exe` file, and a window should appear. Select a file to encrypt and a file to save the result to. Optionally, select a key and algorithm to use. Press `GO!`, and EYECRYPT will encrypt the image and save the result to the file you specified.

![](https://github.com/espimyte/eyecrypt/blob/main/assets/eyecrypt-demo.gif?raw=true)

The key can be a hexadecimal of any length. You can use the `random` button to generate a random key!
Using the same key and algorithm on the same image and the same output file type should always produce the same result.

For more advanced options, the `Show non-ECB` checkbox will allow you to select from non-ECB encryption algorithms.

> [!NOTE]  
> It is reccomended to use smaller, high contrast images if you wish to see more discernable results. Photos, large images, and/or images with a lot of noise tend to produce more obfuscated results...though there are exceptions!

### CLI
<img src="https://github.com/espimyte/eyecrypt/blob/main/assets/eyecrypt-cli-icon.png?raw=true" style="width: 50px; image-rendering: pixelated"></img>

The CLI (command line interface) version is a version designed for the command line. 

This is an option provided for users that for any reason would require/prefer the ability to use EYECRYPT in the command line.

Unlike the GUI version, the CLI version allows you to specify the iv and nonce values, in addition to the key.

The CLI version of EYECRYPT can simply be ran by calling the path to the `eyecrypt.exe` file from the command line.

If you wish to be able to call EYECRYPT from anywhere, you can add the folder that contains the `eyecrypt.exe` file to your `PATH`. If done successfuly, you should be able to run the program from anywhere using `eyecrypt`.

You may require a system restart after adding the program to the `PATH` before using it.

#### Usage Examples
- `eyecrypt -in "input.png" -out "output.png"`
- `eyecrypt -in "png-image.png" -out "jpg-image.jpg"`
- `eyecrypt -in "input.png" -out "output.jpg" -algo camellia-128-ecb` specify an algorithm
- `eyecrypt -in "input.png" -out "output.jpg" -algo cast5-ecb -key FFD1DC` specify a key
- `eyecrypt -in "input.png" -out "output.jpg" -algo aes-128-cbc -key ffa -iv 111` specify an iv for algorithms that use it
- `eyecrypt -in "input.png" -out "output.jpg" -algo sm4-ctr -key 99a -nonce a1` specify a nonce for algorithms that use it
- `eyecrypt -list` print out a list of all supported algorithms

By default, EYECRYPT uses `aes-128-ecb`, with key `0x00000000000000000000000000000000`, and iv/nonce of `0x00000000000000000000000000000000` (if applicable).

Keys, ivs, and nonce values can be any valid hexadecimal.

## SUPPORTED ALGORITHMS

**ECB** = `aes-128-ecb, aes-192-ecb, aes-256-ecb, camellia-128-ecb, camellia-192-ecb, camellia-256-ecb, seed-ecb, sm4-ecb, cast5-ecb, bf-ecb, idea-ecb, des3-64-ecb, des3-128-ecb, des3-192-ecb`

**CBC** = `aes-128-cbc, aes-192-cbc, aes-256-cbc, camellia-128-cbc, camellia-192-cbc, camellia-256-cbc, seed-cbc, sm4-cbc, cast5-cbc, bf-cbc, idea-cbc, des-64-cbc, des3-128-cbc, des3-192-cbc`

**CTR** = `aes-128-ctr, aes-192-ctr, aes-256-ctr, camellia-128-ctr, camellia-192-ctr, camellia-256-ctr, sm4-ctr`

**OFB** = `aes-128-ofb, aes-192-ofb, aes-256-ofb, camellia-128-ofb, camellia-192-ofb, camellia-256-ofb, seed-ofb, sm4-ofb, cast5-ofb, bf-ofb, idea-ofb, des3-64-ofb, des3-128-ofb, des3-192-ofb`

**CFB** = `aes-128-cfb, aes-192-cfb, aes-256-cfb, camellia-128-cfb, camellia-192-cfb, camellia-256-cfb, seed-cfb, sm4-cfb, cast5-cfb, bf-cfb, idea-cfb, des3-64-cfb, des3-128-cfb, des3-192-cfb`

**OTHER** = `rc-40, rc4-56, rc4-64, rc4-80, rc4-128, rc4-192, rc4-256`

## SUPPORTED FILE TYPES
- PNG `.png`
- JPG `.jpg`
- JPEG `.jpeg`
- BMP `.bmp`
- WEBP `.webp`
- APNG `.apng`

Do note that even if the image is output to APNG, it is unlikely to preserve its animation if it had any.

## EXAMPLES

| Original Image  | Result | Parameters |
| ------------- | ------------- | ------------- |
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/example.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/example-result1.png?raw=true)   | **Algorithm:**<br>aes-128-ecb<br><br>**Key:**<br>7b36c46f46f7d4b996f6a153449b0ff1<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/example.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/example-result2.png?raw=true)   | **Algorithm:**<br>idea-ecb<br><br>**Key:**<br>89ce9df4007f31d9b595801a0a23f57c)<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/blossom.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/blossom-result.png?raw=true)   | **Algorithm:**<br>aes-128-ecb<br><br>**Key:**<br>9d836673949da1c27c07c80d26026614<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/rearranger.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/rearranger-result.png?raw=true)   | **Algorithm:**<br> cast5-ecb<br><br>**Key:**<br>231e217c1fdc03c85fede5c0e12ea010<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/vacuum.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/vacuum-result.png?raw=true)   | **Algorithm:**<br> bf-ecb<br><br>**Key:**<br>231e217c1fdc03c85fede5c0e12ea010<br>|
| ![](https://github.com/espimyte/eyecrypt/blob/main/assets/izzy.png?raw=true)  | ![](https://github.com/espimyte/eyecrypt/blob/main/assets/izzy-result.png?raw=true)   | **Algorithm:**<br>sm4-ecb<br><br>**Key:**<br> 28db7fec544231dc31520b7978feaacb<br>|


## ADDITIONAL NOTES

### Compability
This program has only been tested on Windows. I cannot guarantee that it works on other operating systems.

Windows may sometimes prevent the app from running. If this occurs, you can run the program by clicking on `More info`, then clicking `Run anyway`.

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
