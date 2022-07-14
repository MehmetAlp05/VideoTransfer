const { Base64 } = require('js-base64')
const fs = require('fs'),
  path = require('path')
let videoToText = () => {
  let file = fs.readFileSync('something.webm', { encoding: 'base64' })
  fs.writeFileSync('something.txt', file)
}
let textToVideo = () => {
  let file = fs.readFileSync('something.txt', 'utf-8')
  file = file.toString()
  file = Base64.decode(file)
  fs.writeFileSync('something.mp4', file, 'base64')
}
textToVideo()
