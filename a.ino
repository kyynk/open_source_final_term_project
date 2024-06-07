#include <Servo.h> //Build in function
#include <Ultrasonic.h>

Servo myservo;  // 建立SERVO物件
Ultrasonic ultrasonic(11, 12);
int distance;

void setup() {
  Serial.begin(9600);
  myservo.attach(8);  // 設定要將伺服馬達接到哪一個PIN腳
}

void motor_up(int angle){
  myservo.write(0);  //旋轉到0度，就是一般所說的歸零
  delay(1000);
  myservo.write(angle);
}

void loop() {
  distance = ultrasonic.read(); //不加參數就是輸出CM，可用read(INC)輸出英寸
  Serial.print("Distance in CM: ");
  Serial.println(distance);
  delay(500); //每次間格0.5秒
  if(distance < 16){
    motor_up(90);
    delay(1000);
  }
}
