About "msvs2012-2013"
=================
This branch is forked from [codeboost/opencv-node](https://github.com/codeboost/opencv-node).  
The purpose is to use it on Windows and Visual Studio 2012/2013.  

It seems like ok in basic usage, but still needs test.

Now testing on...  
Windows 8 64bit  
node@0.10.23  
npm@1.3.17  
node-gyp@0.12.2  
Visual Studio 2012 + OpenCV 2.4.4(Pre-built)  
Visual Studio 2012 + OpenCV 2.4.7(Pre-built)  
Visual Studio 2013 + OpenCV 2.4.7(Own build)  
only.

If you are Windows user, please try this branch.  
Any bug report/question/advice issues are welcome :)

---------------------------------------------------

The following is original(upstream) README

Purpose
=======
Expose opencv to the node environment.

Features
========
	
	- cv::Point, cv::Size, cv::Rect, etc replaced by object notation:
		Point -> {x: 0, y:0}, Size -> {width: 33, height: 33}

	- Checks the types of parameters as well as ranges of values on each native call (harder to crash app from script)
	- Friendly exception messages on invalid parameters 

Example
=======

See scripts/effects.coffee for a full demo.


Installation - MacOS X 
=======================

	$ brew install opencv --build32
	$ npm install -g opencv-node
	$ coffee scripts/tests

(tested with GCC 4.2.1 and node 0.8.0)

Troubleshooting

If brew complains "SHA1 mismatch" error you may find that updating homebrew fixes the issue:
  $ brew update

If brew complains "No available formula" you will need to tap the science repository:
  $ brew tap homebrew/science

Installation - Windows 
=======================
1. Download OpenCV from http://sourceforge.net/projects/opencvlibrary/files/latest/download
2. Extract it to a folder, eg C:\OpenCV
3. Open a Visual Studio command prompt and type

		set OPENCV_ROOT=C:/OpenCV
		npm install -g opencv-node

(tested with Visual Studio 2010 and node 0.8.8)

API Differences

Some functions have a more js-friendly API/syntax. 
The void functions which return their output in an argument passed by reference, return the result directly:

	cv::split returns an Array and takes only 1 argument
	cv::HoughCircles returns an Array
	cv::HoughLines returns an Array
	cv::cornerSubPix returns an Array

	* others?

License
=======
BSD

Disclaimer
==========

Please report any bugs or missing functions. This module has never been used in production and is generally 
meant to be used for experimentation. 

