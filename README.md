Automatic Wallpaper Change
===
###### Tags: `Ubuntu` `Wallpaper` `Python` `Shell`

Announcement
---
* Base on **Ubuntu 18.04**
* Only **.jpg** and **.png** files can be placed in the image folder

Hands On
---
不想在涼爽的週末做擾人的研究，於是參考網路上各位大神如何更改 Ubuntu 桌布，大多都是下載第三方軟體進而達到更換桌布的功能。於是決定試著更改系統讀取檔案，發現 Ubuntu 是直接讀取 **bionic.xml** 的敘述檔，想說可以更改裡面的圖片路徑，讓系統直接讀取我喜歡的圖片當作桌布，但是有好多張照片的路徑要複製貼上，等做完之後應該就已經虛脫了，既然都是重複的指令，就想用python撰寫程式碼幫我完成這個枯燥乏味的工作，最後在利用 shell 腳本指令將 **bionic.xml** 檔案輕鬆搬運到 `/usr/share/backgrounds/contest/` ，這樣就可以讓系統自動變更喜愛的桌布。

## Download the code
```bash
$ cd ~/Pictures
$ git clone https://github.com/Circle-Kai/automatic_wallpaper_change.git
$ cd ~/Picturesautomatic_wallpaper_change
```
## Create a bionic.xml
```bash
$ python3 main.py  # Make your own bionic.xml file
```

## Keep the original file
```bash
$ source copy_bionic.xml.sh
```

## Replace the original file
```bash
$ source cover_bionic.xml.sh
```
## Reboot your computer
```bash
$ sudo reboot
```
