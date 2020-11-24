
/* Modelo de Código para Controle de Carro c/ Arduino */
 
// Definir os pinos de utilização do Driver L298.
#define pin1 5
#define pin2 6
#define pin3 7
#define pin4 8 
// Variáveis Úteis
int state_temp;
int vSpeed = 200;   // Define velocidade padrão 0 - 255.
char state;
 
void setup() {
  // Inicializar as portas como entrada e saída.
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);
  pinMode(pin4,OUTPUT);
  // Inicializar a comunicação serial.
  Serial.begin(9600);
  
}
 
void loop() {
 
  // Salva os valores da variável 'state'
  if (Serial.available() > 0) {
    state_temp = Serial.read();
    state = state_temp;
  }
 
  // Se o estado recebido for igual a '8', o carro se movimenta para frente.
  if (state == '8') {
    Serial.println("Comando para Frente");
    // Comandos de Motores
    analogWrite(pin1, vSpeed);
    digitalWrite(pin2, LOW);
    analogWrite(pin3, vSpeed);
    digitalWrite(pin4, LOW);
  }
    // Se o estado recebido for igual a '7', o carro se movimenta para Frente Esquerda.
    else if (state == '7') {  
      Serial.println("Comando para Frente-Esquerda");
      // Comandos de Motores
      analogWrite(pin1, vSpeed);
      digitalWrite(pin2, LOW);
      analogWrite(pin3, vSpeed/2);
      digitalWrite(pin4, LOW);
  }
    // Se o estado recebido for igual a '9', o carro se movimenta para Frente Direita.
    else if (state == '9') {   
    Serial.println("Comando para Frente-Direita");
      // Comandos de Motores
    analogWrite(pin1, vSpeed/2);
    digitalWrite(pin2, LOW);
    analogWrite(pin3, vSpeed);
    digitalWrite(pin4, LOW);
  }
  // Se o estado recebido for igual a '2', o carro se movimenta para trás.
  else if (state == '2') { 
    Serial.println("Comando para Trás");
      // Comandos de Motores
    digitalWrite(pin1, LOW);
    analogWrite(pin2, vSpeed);
    digitalWrite(pin3, LOW);
    analogWrite(pin4, vSpeed);
  }
   // Se o estado recebido for igual a '1', o carro se movimenta para Trás Esquerda.
   else if (state == '1') {  
    Serial.println("Comando para Trás-Esquerda");
      // Comandos de Motores
    digitalWrite(pin1, LOW);
    analogWrite(pin2, vSpeed/2);
    digitalWrite(pin3, LOW);
    analogWrite(pin4, vSpeed);
  }
  // Se o estado recebido for igual a '3', o carro se movimenta para Trás Direita.
  else if (state == '3') {  
    Serial.println("Comando para Trás-Direita");
      // Comandos de Motores
    digitalWrite(pin1, LOW);
    analogWrite(pin2, vSpeed);
    digitalWrite(pin3, LOW);
    analogWrite(pin4, vSpeed/2);
  }
  // Se o estado recebido for igual a '4', o carro se movimenta para esquerda.
  else if (state == '4') {   
    Serial.print("Comando para Esquerda");
      // Comandos de Motores
    analogWrite(pin1, vSpeed);
    digitalWrite(pin2, LOW);
    digitalWrite(pin3, LOW);
    digitalWrite(pin4, LOW);
  }
  // Se o estado recebido for igual a '6', o carro se movimenta para direita.
  else if (state == '6') {   
    Serial.println("Comando para Direita");
      // Comandos de Motores
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, LOW);
    analogWrite(pin3, vSpeed);
    digitalWrite(pin4, LOW);
  }
  // Se o estado recebido for igual a '5', o carro permanece parado.
  else if (state == '5') {   
    Serial.print("Comando para Parar");
      // Comandos de Motores
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, LOW);
    digitalWrite(pin3, LOW);
    digitalWrite(pin4, LOW);
  }
}
