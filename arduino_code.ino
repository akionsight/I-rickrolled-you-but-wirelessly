int lightPin = A0;
int lightVal;
int buzzPin = 6;

void setup () {
  
  pinMode(lightPin, INPUT);
  pinMode(buzzPin, OUTPUT);
  
  Serial.begin(9600);
  
}

void loop () {

  lightVal = analogRead(lightPin);

  Serial.println(lightVal);
}
