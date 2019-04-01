# -*- coding: pyxl -*-
from pyxl import html
from PIL import Image
from tqdm import tqdm
import os

class WAImg:
  def __init__(self, num):
    self.num = num
    self.srcImage = Image.open(str(self.num) + ".jpg")
    self.sizes = set()
    
  def generateFiles(self):
    (origW, origH) = self.srcImage.size
    w = origW
    while w > 300:
      self.sizes.add(w)
      if not os.path.isfile("%i-%i.jpg" % (self.num, w)):
        h = int(origH * w / origW)
        resizedImage = self.srcImage.resize((w, h), Image.BICUBIC)
        resizedImage.save("%i-%i.jpg" % (self.num, w))
      w = int(w / 1.4)
      
  def imgElement(self):
    (origW, origH) = self.srcImage.size
    srcset = ", ".join(["%i-%i.jpg %iw" % (self.num, w, w) for w in self.sizes])
    src = "%i-%i.jpg" % (self.num, max(self.sizes))
    return <img data-srcset="{srcset}" data-ar="{origW / origH}" data-src="{src}" />

def main():
  # Intentionally omitted: 31, 33, 3, 50, 72
  nums = [13, 83, 103, 64, 91, 56, 21, 100, 95, 85, 45, 104, 8, 77, 92, 61, 88, 57, 84, 71, 51, 73, 26, 12, 68, 1, 99, 70, 9, 35, 80, 96, 38, 62, 36, 5, 59, 78, 60, 82, 52, 53, 40, 2, 97, 7, 41, 49, 43, 106, 44, 46, 6, 48, 81, 69, 47, 90, 37, 107, 39, 34, 86, 67, 55, 32, 108, 75, 30, 29, 76, 20, 87, 28, 66, 27, 25, 79, 23, 24, 109, 22, 58, 19, 65, 74, 94, 105, 11, 93, 54, 17, 98, 63, 16, 110, 15, 102, 14, 101, 18, 89, 10, 42, 4]
  WAImages = [WAImg(n) for n in nums]
  imgElements = <frag></frag>
  
  for img in tqdm(WAImages, desc="Images"):
    img.generateFiles()
    imgElements.append(img.imgElement())
    
  gaScript1 = <script src="https://www.googletagmanager.com/gtag/js?id=UA-123337994-2"></script>
  gaScript2 = <script>{html.rawhtml("""window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'UA-123337994-2');""")}</script>
  
  gaScript1.set_attr("async", "") # async is a Python keyword, so we have to set this attribute manually  
  
  doc = (
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        {gaScript1}
        {gaScript2}
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>
          Photos | Alicia Torres and William Hoza's Wedding Website
        </title>
        <link href="https://fonts.googleapis.com/css?family=PT+Sans" rel="stylesheet" />
        <link rel="stylesheet" href="/assets/index2.css" />
        <link rel="stylesheet" href="index.css" />
      </head>
      <body>
        <div id="flow">
          <header>
            <div id="header-event-basics">
              <time datetime="2019-11-08" style="margin-right:20px;">November 8, 2019</time>
              Austin, TX
              <span style="float:right;">
                &num;cavemanandwife2019
              </span>
            </div>
            <div id="h1-line">
              <h1>
                ALICIA &amp; WILLIAM
              </h1>
              <button id="nav-show-button" onclick="showNav();">Menu</button>
            </div>
            <nav>
              <div><button id="nav-hide-button" onclick="hideNav();">Hide</button></div>
              <div><a href="/">HOME</a></div>
              <div><a href="/wedding-party/">WEDDING PARTY</a></div>
              <div><a href="/photos/">PHOTOS</a></div>
              <div><a href="/our-catholic-wedding/">OUR CATHOLIC WEDDING</a></div>
              <div><a href="/places-of-interest/">PLACES OF INTEREST</a></div>
            </nav>
          </header>
          <main>
            <h2>
              PHOTOS
            </h2>
            <div id="image-data">
              {imgElements}
            </div>
            <div id="gallery">
            </div>
          </main>
        </div>
        
        <script src="index.js"></script>
        <script src="/assets/index.js"></script>
      </body>
    </html>
  )
  
  file = open("index.html", "w")
  file.write("<!DOCTYPE html>" + str(doc))

if __name__ == "__main__":
  main()
