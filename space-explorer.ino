int buttonValue = 0;
int potValue = 0;
int potLeft = 0;
int potRight = 0;
int outputValue = 0;
int sw = 0;
int xRead = 0;
int xfactorlow = 0;
int xfactorhigh = 0;
int vX = 0;
int yRead = 0;
int yfactorlow = 0;
int yfactorhigh = 0;
int vY = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000); // give me time to bring up serial monitor
}

void loop() {
  // put your main code here, to run repeatedly:

  // read button value
  pinMode(26, INPUT_PULLUP);
  buttonValue = digitalRead(26);

  // read potentiometer value
  potValue = analogRead(12);
  potLeft = map(potValue, 0, 1900, -10, 1);
  potRight = map(potValue, 2100, 4095, 1, 10);

  if (potValue < 1900) {
    potValue = -1 * potLeft;
  } else if (potValue > 2100) {
    potValue = -1 * potRight;
  } else {
    potValue = 0;
  }

  // read joystick value
  sw = digitalRead(15);

  xRead = analogRead(13);
  yRead = analogRead(25);

  xfactorlow = map(xRead, 0, 1955, -10, -1);
  xfactorhigh = map(xRead, 1975, 4095, 1, 10);
  yfactorlow = map(yRead, 0, 1885, -10, -1);
  yfactorhigh = map(yRead, 1905, 4095, 1, 10);
  
  if (xRead < 1955) {
    vX = xfactorlow;
  } else if (xRead > 1975) {
    vX = xfactorlow;
  } else {
    vX = 0;
  }

  if (yRead > 1905) {
    vY = -1 * yfactorhigh;
  } else if (yRead < 1885) {
    vY = -1 * yfactorlow;
  } else {
    vY = 0;
  }

  // fix dial error value
  if (potValue == 10) {
    potValue = 0;
  }

  // form a JSON-formatted string:
  String jsonString = "{\"button\":\"";
  jsonString += buttonValue;
  jsonString +="\",\"dial\":\"";
  jsonString += potValue;
  jsonString +="\",\"vY\":\"";
  jsonString += vY;
  jsonString +="\",\"vX\":\"";
  jsonString += vX;
  jsonString +="\",\"switch\":\"";
  jsonString += sw;
  jsonString +="\"}";

  // print it:
  Serial.println(jsonString);
 
  //delay(500);
}
