cv = require './opencv'

Mat = cv.Mat
console.log cv

cv.namedWindow "original", 0
cv.namedWindow "dest", 0

src = new Mat 320, 240
dest = new Mat 320, 240

console.log 'Copying to dest '
src.copyTo dest

cv.imshow("original", src);

console.log 'Copied'
