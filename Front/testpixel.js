/* TORI:
   1) setup() & draw() loops
	 2) createCanvas(550, 500);
      background(255);
      noStroke();
	 3) rects()
	 4) fills()
	 5) if (mouseIsPressed) {
        if (mouseX < 50) {
          if (mouseY < 50) {
            fill(75, 0, 130);
        }
*/
l
let red = [];
let green = [];
let blue = [];



function setup() {

	createCanvas(550, 500);
	rectMode(CENTER);

	s = 5
	xmax = round(width / s)
	ymax = round(height / s)
	v = createVector(xmax, ymax);
		background(255);

	  for (let x = 0; x < xmax; x++) {
    red[x] = []; // create nested array
		green[x] = []; // create nested array
		blue[x] = []; // create nested array

    for (let y = 0; y < ymax; y++) {
      red[x][y] = random(0, 255);
      green[x][y] = random(0, 255);
      blue[x][y] = random(0, 255);
			fill(red[x][y],green[x][y] ,blue[x][y] )
			rect(x*s, y*s, s, s);

		}
  }


	noStroke();
	fill(75, 0, 130);
	rect(0, 0, 50, 50);
	fill(148, 0, 211);
	rect(0, 50, 50, 50);
	fill(0, 255, 255);
	rect(0, 100, 50, 50);
	fill(0, 0, 255);
	rect(0, 150, 50, 50);
	fill(0, 255, 0);
	rect(0, 200, 50, 50);
	fill(255, 255, 0);
	rect(0, 250, 50, 50);
	fill(255, 127, 0);
	rect(0, 300, 50, 50);
	fill(255, 0, 0);
	rect(0, 350, 50, 50);
	fill(0, 0, 0);
	rect(0, 400, 50, 50);
	fill(230, 230, 230);
	rect(0, 450, 50, 50);
}

function draw() {
	if (mouseIsPressed) {
		if (mouseX < 50) {
			if (mouseY < 50) {
				fill(75, 0, 130);
			}
			if (mouseY > 50 && mouseY < 100) {
				fill(148, 0, 211);
			}
			if (mouseY > 100 && mouseY < 150) {
				fill(0, 255, 255);
			}
			if (mouseY > 150 && mouseY < 200) {
				fill(0, 0, 255);
			}
			if (mouseY > 200 && mouseY < 250) {
				fill(0, 255, 0);
			}
			if (mouseY > 250 && mouseY < 300) {
				fill(255, 255, 0);
			}
			if (mouseY > 300 && mouseY < 350) {
				fill(255, 127, 0);
			}
			if (mouseY > 350 && mouseY < 400) {
				fill(255, 0, 0);
			}
			if (mouseY > 400 && mouseY < 450) {
				fill(0, 0, 0);
			}
			if (mouseY > 450 && mouseY < 500) {
				fill(230, 230, 230);
			}
		}
		x = round(mouseX / s)
		y = round(mouseY / s)
		//red[x][y] = 

		if (mouseIsPressed) {
			if (mouseX > 50) {
				rect(x*s, y*s, s, s);
			}
		}
	}
}
