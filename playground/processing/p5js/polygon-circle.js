/*jshint esversion: 6 */

// polygon array and number of verts
let poly = []
let n = 100 // feel free to play with this number :)

// canvas size variables
let w = 500
let h = 500

// oscillators
let chord = []
let root = 30
let major = [ 4, 5, 6 ]
let minor = [ 10, 12, 15 ]

// setup and draw functions ---

function setup() {
  createCanvas(w, h)
  strokeWeight(12)
  noFill()
  cursor(HAND)
  noStroke()
  n++ // add extra point for closing the polygon

  for (let i = 0; i < n; i++) {
    // populate regular polygon vertices given number of points n
  	let a = {
      x: (w/2) + 100*sin(map(i, 0, n-1, 0, TAU)),
      y: (h/2) + 100*cos(map(i, 0, n-1, 0, TAU))
    }
  	poly.push(a)
  }

  // initialize oscillators
  if (n < 25) {
    for (let i = 0; i < 3; i++)
    	chord[i] = new p5.TriOsc()
  } else {
    for (let i = 0; i < 3; i++)
    	chord[i] = new p5.SinOsc()
  }

  // initialize with major chord intervals
  for (let i = 0; i < chord.length; i++) {
    	chord[i].freq(major[i] * root)
        chord[i].amp(0.0)
  		chord[i].stop()
  }
}

function draw() {
  // use default blend mode for background
  blendMode(BLEND)
  background(0, 0, 0)

  // use additive blend mode to separate color channels
  blendMode(ADD)
  stroke(255, 0, 0)
  drawPoly(1000, 1000)

  stroke(0, 255, 0)
  drawPoly(1200, 1500)

  stroke(0, 0, 255)
  drawPoly(2000, 1700)

  // distort oscillatiors
  warpOsc()
}


// helper function implementations ---

function logMap(value, start1, stop1, start2, stop2) {
  // based off of linear regression + existing p5.map function
  start2 = log(start2)
  stop2 = log(stop2)

  return exp(start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1)))
}

function drawPoly(dx, dy) {
  // draws polygon given vertices in the poly[] array, adds mouse bias using params

  let g = 0
  if (mouseIsPressed)
    g = random(-2, 2)

  beginShape()
  for (let i = 0; i < n; i++) {
  	let bias = dist(mouseX, mouseY, poly[i].x, poly[i].y)
  	vertex(poly[i].x + dx / logMap(bias, w, 0, dx, 45) + g, poly[i].y + dy / logMap(bias, h, 0, dy, 45) + g)
  }
  endShape()
}

function warpOsc() {
  // uses max dist to determine the frequency distortion

  let bias = 0
  for (let i = 0; i < n; i++)
  	bias = max(bias, dist(mouseX, mouseY, poly[i].x, poly[i].y))

  for (let i = 0; i < chord.length; i++)
    chord[i].freq(map(bias, w, 0, major[i], minor[i]) * root)
}

function mousePressed() {
  // toggles synths on

  for (let i = 0; i < chord.length; i++) {
    chord[i].start()
    chord[i].amp(0.3, 0.5)
  }
}

function mouseReleased() {
  // toggles synths off

  for (let i = 0; i < chord.length; i++) {
    chord[i].amp(0.0, 0.05)
    chord[i].stop()
  }
}
