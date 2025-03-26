/**
 * Bounce. 
 * 
 * When the shape hits the edge of the window, it reverses its direction. 
 */
import java.util.ArrayList;


int rad = 60;        // Width of the shape
float xpos, ypos;    // Starting position of shape    

float xspeed = 2.8;  // Speed of the shape
float yspeed = 2.2;  // Speed of the shape

int xdirection = 1;  // Left or Right
int ydirection = 1;  // Top to Bottom



int adjust = 60;
int topAdjust = 60;
float extraAdjust = 1;
int time = 0;
int totalTopEnd = 0;
int totalBotEnd = 0;

//x, y, t=1.0/f=0.0, r ,g, b
//float[][] mpArr = { {0.0, 0.0, 1.0,   50,50,50} };
//ArrayList<String> cars = new ArrayList<String>(); // Create an ArrayList object
ArrayList<ArrayList<Float>> mpArr = new ArrayList<ArrayList<Float>>();
ArrayList<Float> temp = new ArrayList<Float>();


int riverLength = 1500;

void setup(){
  
  temp.add(0.0);//x
  temp.add(0.0);//y
  temp.add(1.0);//exists
  temp.add(50.0);//r
  temp.add(50.0);//g
  temp.add(50.0);//b
  mpArr.add(temp);
  System.out.println(mpArr);
  size(1535, 860);
  noStroke();
  frameRate(30);
  ellipseMode(RADIUS);
  // Set the starting position of the shapes   https://hianime.to/watch/the-dungeon-of-black-company-15801?ep=81443&ep=81443
  xpos = width/2;
  ypos = height/2;
}

void draw() 
{
  time++;
  background(220);
  
  stroke(0);
    strokeWeight(8);
    
    line(-20, 404+topAdjust, 2000, 404+topAdjust);
    
    noStroke();
    
    fill(69, 91, 255);
    rect(100, 300+topAdjust, riverLength, 100);
    
    
    strokeWeight(2);
    stroke(0,0,0);
    
    
    float mpLevelTOP = 0.0;
    float pastLevelTOP = 0.0;
    float mpLevelBOT = 0.0;
    float pastLevelBOT = 0.0;
                        
  for(int i = riverLength; i > 100; i--){
    for(int j = 0; j < mpArr.size(); j++){
      if (abs(mpArr.get(j).get(0) - i) < 12 && mpArr.get(j).get(1) < 400+topAdjust && mpArr.get(j).get(2) == 1.0){
        mpLevelTOP -=10*extraAdjust;
      }
      else if(abs(mpArr.get(j).get(0) - i) < 12 && mpArr.get(j).get(1) > 400+topAdjust && mpArr.get(j).get(2) == 1.0){
        mpLevelBOT -=10*extraAdjust;
              }
    }
    
    if(mpLevelTOP*extraAdjust < -260 || mpLevelBOT*extraAdjust < -260){
      extraAdjust*= 0.96;
    }
    //mpLevel = 100+((i)*(0.2));
    strokeWeight(1);
    line(i+1, extraAdjust*(pastLevelTOP)+300+topAdjust, i, extraAdjust*(mpLevelTOP)+300+topAdjust);
    line(i+1, extraAdjust*(pastLevelBOT)+700+adjust, i, extraAdjust*(mpLevelBOT)+700+adjust);
    
    if(i == 101){
      totalTopEnd += mpLevelTOP;
      totalBotEnd += mpLevelBOT;
    }
    
    //point(i, 300+mpLevel);
    pastLevelTOP = mpLevelTOP;
    pastLevelBOT = mpLevelBOT;

    mpLevelTOP = 0;
    mpLevelBOT = 0;

  }/////////////////////////////////////////
            /*                        
  for(int i = riverLength; i > 100; i--){/////////////////////////////////////
    for(int j = 0; j < mpArr.size(); j++){
      if (abs(mpArr[j][0] - i) < 12 && mpArr[j][1] < 400+topAdjust && mpArr[j][2] == 1.0){
        mpLevelTOP -=10*extraAdjust;
      }
      else if(abs(mpArr[j][0] - i) < 12 && mpArr[j][1] > 400+topAdjust){
        mpLevelBOT -=10*extraAdjust;
              }
    }
    
    if(mpLevelTOP*extraAdjust < -260 || mpLevelBOT*extraAdjust < -260){
      extraAdjust*= 0.96;
    }
    //mpLevel = 100+((i)*(0.2));
    strokeWeight(1);
    line(i+1, extraAdjust*(pastLevelTOP)+300+topAdjust, i, extraAdjust*(mpLevelTOP)+300+topAdjust);
    line(i+1, extraAdjust*(pastLevelBOT)+700+adjust, i, extraAdjust*(mpLevelBOT)+700+adjust);
    
    if(i == 101){
      totalTopEnd += mpLevelTOP;
      totalBotEnd += mpLevelBOT;
    }
    
    //point(i, 300+mpLevel);
    pastLevelTOP = mpLevelTOP;
    pastLevelBOT = mpLevelBOT;

    mpLevelTOP = 0;
    mpLevelBOT = 0;

  }/////////////////////////////////////////
  */
  for(int i = 0; i < mpArr.size(); i++){
      stroke(mpArr.get(i).get(3), mpArr.get(i).get(4), mpArr.get(i).get(5));
      strokeWeight(2);
      if(mpArr.get(i).get(2) == 1.0){
        point(mpArr.get(i).get(0), mpArr.get(i).get(1));
      }
        mpArr.get(i).set(0, mpArr.get(i).get(0) - 0.5); //-=0.5;
      
      if( mpArr.get(i).get(0) % (riverLength/10) < 1 && random(0,1) < 1 && mpArr.get(i).get(1) < 400+topAdjust){
         mpArr.get(i).set(2, 0.0);
         }
    
  }
  
  for (int i = 0; i < 4; i++){
    //float[] temp = {random(110, riverLength), random(310+topAdjust,390+topAdjust), true, random(0,255),random(0,255),random(0,255)};
    ArrayList<Float> temp1 = new ArrayList<Float>();
    temp1.add(random(110, riverLength));//x
    temp1.add(random(310+topAdjust,390+topAdjust));//y
    temp1.add(1.0);//exists
    temp1.add(random(0,255));//r
    temp1.add(random(0,255));//g
    temp1.add(random(0,255));//b
    mpArr.add(temp1);
    
    //append(mpArr, [random(110, length), random(310+topAdjust,390+topAdjust), true, [random(0,255),random(0,255),random(0,255)]])
  }
  
  noStroke();

  fill(69, 91, 255);
  rect(100, 700+adjust, riverLength, 100);
  
  
  strokeWeight(2);
  stroke(0,0,0);

  //mpLevel = 0;
  
  
    
  // Update the position of the shape
  xpos = xpos + ( xspeed * xdirection );
  ypos = ypos + ( yspeed * ydirection );
  
  // Test to see if the shape exceeds the boundaries of the screen
  // If it does, reverse its direction by multiplying by -1
  if (xpos > width-rad || xpos < rad) {
    xdirection *= -1;
  }
  if (ypos > height-rad || ypos < rad) {
    ydirection *= -1;
  }

  // Draw the shape
  ellipse(xpos, ypos, rad, rad);
}
