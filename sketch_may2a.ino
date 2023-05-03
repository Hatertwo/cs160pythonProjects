int val_pot;
int max_val = 930;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A1, INPUT);
  pinMode(12, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(4, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  val_pot = analogRead(A1);
  // Serial.print("The digital value is: ");
  // Serial.println(val_pot);
  // delay(1000);
  if (val_pot > max_val / 3){
    digitalWrite(4, HIGH);
      if (val_pot > max_val * 2 / 3) {
        digitalWrite(8, HIGH);
        if (val_pot > max_val) {
        digitalWrite(12, HIGH);
      } else {
        digitalWrite(12, LOW);
     }
    } else {
    digitalWrite(8, LOW);
    }
   } else {
    digitalWrite(4, LOW);
  }
}
