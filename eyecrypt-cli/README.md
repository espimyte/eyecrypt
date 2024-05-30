Thank you for downloading EYECRYPT!

---

The CLI version of EYECRYPT can simply be ran by calling the path to the eyecrypt.exe file from the command line.

If you wish to be able to call EYECRYPT from anywhere, you can add the folder that contains the eyecrypt.exe file to your PATH.
If done successfuly, you should be able to run the program from anywhere using eyecrypt.
You may require a system restart after adding the program to the PATH before using it.

Usage Examples:

    eyecrypt -in "input.png" -out "output.png"
    eyecrypt -in "png-image.png" -out "jpg-image.jpg"
    eyecrypt -in "input.png" -out "output.jpg" -algo camellia-128-ecb specify an algorithm
    eyecrypt -in "input.png" -out "output.jpg" -algo cast5-ecb -key FFD1DC specify a key
    eyecrypt -in "input.png" -out "output.jpg" -algo aes-128-cbc -key ffa -iv 111 specify an iv for algorithms that use it
    eyecrypt -in "input.png" -out "output.jpg" -algo sm4-ctr -key 99a -nonce a1 specify a nonce for algorithms that use it
    eyecrypt -list print out a list of all supported algorithms

By default, EYECRYPT uses aes-128-ecb, with key 0x00000000000000000000000000000000, and iv/nonce of 0x00000000000000000000000000000000 (if applicable).
Keys, ivs, and nonce values can be any valid hexadecimal.

---

For additional information, please visit https://github.com/espimyte/eyecrypt.
