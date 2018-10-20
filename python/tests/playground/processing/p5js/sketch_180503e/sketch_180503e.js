var blockSize = 50;
var countBorder = 9;
var wdt = blockSize * countBorder;
var hgt = blockSize * countBorder;
var modes = [semiDual, shark, oneSemi, mess, rotateSemi, pear, chain];
var currModeFn = semiDual;
var colorSchemes = [
  [ '#152A3B', '#158ca7', '#F5C03E', '#D63826', '#F5F5EB' ],
  [ '#0F4155', '#288791', '#7ec873', '#F04132', '#fcf068' ],
  [ '#E8614F', '#F3F2DB', '#79C3A7', '#668065', '#4B3331' ]
];
var queueNum = [ 0, 1, 2, 3, 4 ];
var clrs = colorSchemes[0];

function setup() {
  createCanvas(wdt, hgt);
  rectMode(CENTER);
  noStroke();
  noLoop();
}

function draw() {
  background(25);
  for (var y = blockSize / 2; y < height; y+=blockSize) {
    for (var x = blockSize / 2; x < width; x+=blockSize) {
      queueNum = shuffleArray([ 0, 1, 2, 3, 4 ]);
      fill(clrs[queueNum[0]]);
      rect(x, y, blockSize, blockSize);

      push();
      translate(x, y);
      currModeFn(0, 0, clrs);
      pop();
    }
  }
  paper();
}

function chain(x, y, clrs) {
  rotate(radians(90 * Math.round(random(1, 5))));
  fill(clrs[queueNum[1]]);
  arc(x - blockSize / 2, y, blockSize, blockSize, radians(270), radians(450));
  fill(clrs[queueNum[2]]);
  arc(x + blockSize / 2, y, blockSize, blockSize, radians(90),  radians(270));

  rotate(radians(90 * Math.round(random(1, 5))));
  fill(clrs[queueNum[1]]);
  arc(x, y + blockSize / 2, blockSize, blockSize, radians(180), radians(360));
  fill(clrs[queueNum[2]]);
  arc(x, y - blockSize / 2, blockSize, blockSize, radians(0),   radians(180));
}

function pear(x, y, clrs) {
  rotate(radians(90 * Math.round(random(1, 5))));

  fill(clrs[queueNum[1]]);
  arc(x - blockSize / 2, y, blockSize, blockSize, radians(270), radians(450));
  fill(clrs[queueNum[2]]);
  arc(x + blockSize / 2, y, blockSize, blockSize, radians(90),  radians(270));

  fill(clrs[queueNum[1]]);
  arc(x, y + blockSize / 2, blockSize, blockSize, radians(180), radians(360));
  fill(clrs[queueNum[2]]);
  arc(x, y - blockSize / 2, blockSize, blockSize, radians(0),   radians(180));
}

function rotateSemi(x, y, clrs) {
  rotate(radians(90 * Math.round(random(1, 5))));
  fill(clrs[queueNum[1]]);
  arc(-blockSize / 2, 0, blockSize, blockSize, radians(270), radians(450));
}

function mess(x, y, clrs) {
  fill(clrs[queueNum[Math.floor(random(queueNum.length))]]);
  arc(-blockSize / 2, 0, blockSize, blockSize, radians(270), radians(450));
  for (var i = 0; i < 3; i++) {
    fill(clrs[queueNum[Math.floor(random(queueNum.length))]]);
    rotate(radians(90 * Math.round(random(1, 5))));
    arc(x, y + blockSize / 2, blockSize, blockSize, radians(270), radians(450));
  }
}

function oneSemi(x, y, clrs) {
  if (random(1) > .2) {
    fill(clrs[queueNum[Math.floor(random(queueNum.length))]]);
    arc(x - blockSize / 2, y, blockSize, blockSize, radians(270), radians(450));
  }
}

function shark(x, y, clrs) {
  if (random(1) > .4) {
    fill(clrs[queueNum[Math.floor(random(queueNum.length))]]);
    arc(x, y + blockSize / 2, blockSize, blockSize, radians(270), radians(450));
  }
}

function semiDual(x, y, clrs) {
  rotate(radians(90 * Math.round(random(1, 5))));
  if (random() > .005) {
    fill(clrs[queueNum[1]]);
    arc(x - blockSize / 2, y, blockSize, blockSize, radians(270), radians(450));
    fill(clrs[queueNum[2]]);
    arc(x + blockSize / 2, y, blockSize, blockSize, radians(90),  radians(270));
  }
}

function shuffleArray(array) {
  var j, temp;
  for (var i = array.length - 1; i > 0; i--) {
    j = Math.floor(Math.random() * (i + 1));
    temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }

  return array;
}

function resetPatchwork(modeFn) {
  currModeFn = modeFn || modes[Math.floor(random(modes.length))];
  clrs = colorSchemes[Math.floor(random(colorSchemes.length))];
  redraw();
}

function mousePressed(){
  resetPatchwork();
}

function keyPressed(e){
  switch(e.key.toLowerCase()){
    case '1': resetPatchwork(semiDual); break;
    case '2': resetPatchwork(shark); break;
    case '3': resetPatchwork(oneSemi); break;
    case '4': resetPatchwork(mess); break;
    case '5': resetPatchwork(rotateSemi); break;
    case '6': resetPatchwork(pear); break;
    case '7': resetPatchwork(chain); break;
    case 's': save('img_' + ~~random(100, 900) + '.jpg'); break;
    default: resetPatchwork(); break;
  }
}

function paper() {
  push();
  strokeWeight(1);
  noStroke();
  for (var i = 0; i<width-1; i+=2) {
    for (var j = 0; j<height-1; j+=2) {
      fill(random(205-40, 205+30), 25);
      rect(i, j, 2, 2);
    }
  }

  for (var i = 0; i<30; i++) {
    fill(random(130, 215), random(100, 170));
    rect(random(0, width-2), random(0, height-2), random(1, 3), random(1, 3));
  }

  pop();
}
