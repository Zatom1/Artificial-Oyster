
import java.util.ArrayList;



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
    
    int step = 6;
  for(int i = riverLength; i > 100; i-=step){
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
    line(i+step, extraAdjust*(pastLevelTOP)+300+topAdjust, i, extraAdjust*(mpLevelTOP)+300+topAdjust);
    line(i+step, extraAdjust*(pastLevelBOT)+700+adjust, i, extraAdjust*(mpLevelBOT)+700+adjust);
    
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
  
    noStroke();

  fill(69, 91, 255);
  rect(100, 700+adjust, riverLength, 100);
  
  

    strokeWeight(2);

  for(int i = 0; i < 9; i++){
    stroke(255,0,0);
  line(150+ (riverLength/10)*i, 300+topAdjust, 150+ (riverLength/10)*i, 400+topAdjust);
  }
  textSize(20);
  text("Filtration location", 200, 200);
  stroke(69, 91, 255);
  line(250, 205, 290+5, 340+11);
  line(290+5, 340+11, 270+5, 320+11);
  line(290+5, 340+11, 298+5, 312+11);

  
  stroke(0,0,0);
  
  for(int i = 0; i < mpArr.size(); i++){
      stroke(mpArr.get(i).get(3), mpArr.get(i).get(4), mpArr.get(i).get(5));
      strokeWeight(2);
      if(mpArr.get(i).get(2) == 1.0){
        point(mpArr.get(i).get(0), mpArr.get(i).get(1));
      }
        mpArr.get(i).set(0, mpArr.get(i).get(0) - 0.5); //-=0.5;
      
      if( mpArr.get(i).get(0) % (riverLength/10) < 1 && random(0,1) < 0.9054 && mpArr.get(i).get(1) < 400+topAdjust && time > 40){
         //mpArr.get(i).set(2, 0.0);
         mpArr.remove(i);
         }
      if(mpArr.get(i).get(0) < 0){
        mpArr.remove(i);
      }
    
  }
  
  if(mpArr.size() < 35000){
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
      ArrayList<Float> temp2 = new ArrayList<Float>();
      temp2.add(random(110, riverLength));//x
      temp2.add(random(710+adjust,790+adjust));//y
      temp2.add(1.0);//exists
      temp2.add(random(0,255));//r
      temp2.add(random(0,255));//g
      temp2.add(random(0,255));//b
      mpArr.add(temp2);
    
    //append(mpArr, [random(110, length), random(310+topAdjust,390+topAdjust), true, [random(0,255),random(0,255),random(0,255)]])
    }
  }
  textSize(12);
  text(extraAdjust, 50, 50);
   text(-1*totalTopEnd/time, 150, 50);
  text(-1*totalBotEnd/time, 150, 70);
  text(mpArr.size(), 150, 90);
  text(frameRate, 450, 70);
  textSize(60);
  fill(0);
  text("River After Deployment", 940, 70);
  text("River Before Deployment", 900, 550);

  //mpLevel = 0;
  
    stroke(0);
    strokeWeight(3);
    fill(0);
    line(100, -10, 100, height+10);
    line(100-10, 300+topAdjust, 100+10, 300+topAdjust);
    line(100-10, 700+adjust, 100+10, 700+adjust);

    textSize(24);
    rotate(-1*PI/2);
    text("(Unitless) Particles / Second", -340, 90);
    text("(Unitless) Particles / Second", -760, 90);

    rotate(1*PI/2);
    
}
