int LEDPIN = 4 ;
int LEDPIN2= 6;
int PIN = 1;

void setup() {
  // put your setup code here, to run once:
  pinMode(LEDPIN, OUTPUT);
  pinMode(LEDPIN2, OUTPUT);
  pinMode(4, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (PIN == 1){
    digitalWrite(LEDPIN, HIGH);
    delay(500);
    digitalWrite(LEDPIN, LOW);
    delay(500);
    digitalWrite(LEDPIN2, HIGH);
    delay(500);
    digitalWrite(LEDPIN2, LOW);
    delay(1000);
    digitalWrite(LEDPIN, HIGH);
    delay(1000);
    digitalWrite(LEDPIN, LOW);
    delay(500);
    digitalWrite(LEDPIN2, HIGH);
    delay(500);
    digitalWrite(LEDPIN2, LOW);
    delay(500);
  }
    
}
