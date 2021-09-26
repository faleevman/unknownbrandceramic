/*
This program demonstrates uploading Media Files in JS
using the functions loadImage and image. Due to Asynchronous nature of Javascript, loadImage is called
in preload function before setup is called. Preload is used to load media assets so that they are ready to use in setup and the rest of the program!



 !
  !
   !
   */
let img;
let imgUrl = "";
let xString;
let x;
let y;
let w;
let h;

let idleRed;
let idleRedDir = 40;

let g = 0
let d = 0


//Media assets are loaded here.
function preload() {
}

function setup() {
  var canvas = createCanvas(600, 400);
  canvas.parent('jumbo-canvas')
  // canvas.mouseWheel(changeSize);


  let inp = createInput('');
  inp.parent('jumbo-inp')
  //inp.position(0, 0);
  inp.size(100);
  inp.input(myInputEvent)


  let button = createButton('Proceed to payment');
  button.parent('jumbo-but')
  button.mousePressed(ButtonGo);
  w = width/2;
  h = height/2;
}

function draw() {
  background(0);
  textSize(36)
    text("Рабочии канвас", 20,40)
  

  if (mouseIsPressed && mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height)
  {
      textSize(6)
      text("mouseIsPressed", 500, 350)
      text ("x = " + x,500, 360 )
      text ("y = " + y,500, 370 )
      textSize(36)
       x = mouseX - (w/2);
       y = mouseY - (h/2);
  }
  fill("yellow")
  ellipse(x+ (w/2),y + (h/2),20)
  if (img  != null)
  {
  	  
  	  image(img,x,y,w*g,h*g);
  }
  else
  {
    text ("print image URL",x+ (w/2),y + (h/2) )
    fill(idleRed,50,50)
    idleRed += idleRedDir
    if (idleRed < 0 || idleRed > 255)
      idleRedDir = - idleRedDir
  	text ("frameCount " + frameCount, 20, height - 20)
    ellipse(mouseX,mouseY,idleRed/2)
    fill(200)

  }

}

function keyPressed() {
  if (keyCode == RIGHT_ARROW) {


  g = g + 0.1;
  console.log("g  = ",g)
    if (g > 1.5)
      g = 0.5
  }

}





function myInputEvent() {
  console.log('you are typing: ', this.value());
    //imgUrl = "https://w-dog.ru/wallpapers/5/10/327424753220270/ptica-obyknovennyj-zimorodok-alcedo-atthis-zimorodok-kapli-klyuv-ulov-ryba-vetka.jpg";
    imgUrl = this.value();
    img = createImg(imgUrl,"");

}



function ButtonGo() {
  // let p = createP('это дорого, вы хотите пордолжить?');
  // p.parent('jumbo-p')
  // p.style('font-size', '16px');

	if (imgUrl != "")
		postJSONToServ()
}


function postJSONToServ()
{
	fetch('https://8e80964ec66a8a954a9d2076edd903c5.m.pipedream.net', {
  method: 'POST',
  body: JSON.stringify({
    url: imgUrl,
    x: x,
    y: y,
    
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));

}