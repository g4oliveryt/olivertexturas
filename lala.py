
import pyttsx3
import pyautogui as p
from time import*

engine = pyttsx3.init()
engine.setProperty("rate" , 150)
voz1 = "Antes de comenzar porfavor escrive tu nombre"
engine.say(voz1)
engine.runAndWait()



pr = input("Aqui:")
print("Hola ",pr,"!")
voz2 =  pr , " un gusto en conocerte, bienvenido a setproperty ,donde somos un programa creado con el proposito de mostrarte algunas combinaciones de teclas y algunos trucos de tu ordenador"
engine.say(voz2)
engine.runAndWait()

print("--------------------------------------------------------------------")
print("|                                                                  |")
print("|                           SetProperty                            |")
print("|                                                                  |")
print("--------------------------------------------------------------------")
voz3 = "aqi puedes ver en pantalla las primeras tres conbinaciones que te mostrare"
engine.say(voz3)
engine.runAndWait()
print("Win + D")
print("Ctrl + Win + O")
print("Ctrl + c  Y  Ctrl + v")
voz4 = "Por si no lo sabes, la tecla Win, se encuentra en el teclado con el logo de windows como una banderita."
engine.say(voz4)
engine.runAndWait()
voz5 = "vamos a empezar por la combinacion de windows mas De"
engine.say(voz5)
engine.runAndWait()
print("")
print("Win + D  <----")
voz6 = "la combinacion de windows mas De sirve para minimizar todas la ventanas abiertas de rrepente e actualizar nuestro escritorio"
engine.say(voz6)
engine.runAndWait()
voz7 = "boy a hacer una demostracion para que veas lo que pasa cuando ejecutas la combinacion de teclas, por favor no toques nada y veras como me saca al escritorio"
engine.say(voz7)
engine.runAndWait()
p.hotkey("win" , "d")
voz8 = "Haora por favor regrese a la ventana anterior para que podamos continuar"
engine.say(voz8)
engine.runAndWait()
sleep(6)
voz9 = "muy bien continuemos con la combinacion control mas windows mas oo"
engine.say(voz9)
engine.runAndWait()
print("Ctrl + win + O  <-------")
voz10 = "esta sirve para invocar un teclado en pantalla en caso de que el teclado de tu ordenador no funcione correctamente"
engine.say(voz10)
engine.runAndWait()
voz11 = "y haci se ve el teclado una vez ejecutada la combinacion"
engine.say(voz11)
engine.runAndWait()
p.hotkey("ctrl" , "win" , "o")
sleep(1)
voz12 = "Haora sierre la ventana de el taclado"
engine.say(voz12)
engine.runAndWait()
sleep(4)
voz13 = "muy bien gracias"
engine.say(voz13)
engine.runAndWait()
voz14 = "haora continuemos con las conbinaciones de control mas ube y control mas c"
engine.say(voz14)
engine.runAndWait()
print("Ctrl + v  Y  Ctrl + c <-----------")
voz15 = "Esta es mucha mas popular que las otras debido a su facilidad de usar y que nos brinda copiar datos y pegar de una manera muy sencilla"
engine.say(voz15)
engine.runAndWait()
voz16 = "Solo vasta con seleccionar y apretar control mas ce para copiar y control mas ube para pegar"
engine.say(voz16)
engine.runAndWait()
print("")
print("----------------------------------")
print("|¿Quieres que te siga enseñando? |")
print("----------------------------------")
voz31 = "Quieres continuar con nosotros"
engine.say(voz31)
engine.runAndWait()
voz18 = "si quieres continuar coloca un si , y si quieres salir coloca un no"
engine.say(voz18)
engine.runAndWait()

pregu = input("Quieres continuar: ")
if pregu == "si" or pregu == "SI":
    voz23 = pr, "a continuacion te dire unas preguntas para poder saber si estas aprendiendo, si no estas aprendiendo no dudare en repetirte lo anterior de una manera fluida asta que aprendas"
    engine.say(voz23)
    engine.runAndWait()
    voz17 = "para responder a las preguntas escrive la palabra faltante de las preguntas"
    engine.say(voz17)
    engine.runAndWait()
    
    
    voz25 = "Para que sirve la combinacion windows mas de"
    engine.say(voz25)
    engine.runAndWait()
    p1 = input("¿la combinacion Win + D sirve para minimizar ? ")
    
    if p1 =="ventanas" or p1 == "ventana":
        voz26 = "muy bien"
        engine.say(voz26)
        engine.runAndWait()



    if p1 == "bentanas" or p1 == "bentana":
        voz27 = "muy bien"
        engine.say(voz27)
        engine.runAndWait()


    if p1 == "VENTANAS" or p1 == "VENTANA":
        voz28 = "muy bien"
        engine.say(voz28)
        engine.runAndWait()


    if p1 == "BENTANAS" or p1 == "BENTANA":
        voz29 = "muy bien"
        engine.say(voz29)
        engine.runAndWait()

    if p1 == "las ventanas" or p1 == "LAS VENTANAS":
        voz40 = "muy bien"
        engine.say(voz40)
        engine.runAndWait()


    voz32 = "continuemos con la siguiente pregunta"
    engine.say(voz32)
    engine.runAndWait()


    
    voz31 = " que es lo que muestra en pantalla la combinacion control mas windows mas oo "
    engine.say(voz31)
    engine.runAndWait()
    p2 = input("¿La combinacion (Ctrl + Win + O) sirve para mostrar en pantalla un? ")

    if p2 == "un teclado" or p2 == "UN TECLADO":
        print("")
        print("Correcto!")
        voz33 = "perfecto",pr, "veo que estas aprendiendo"
        engine.say(voz33)
        engine.runAndWait()

    if p2 == "teclado" or p2 == "TECLADO":
        print("")
        print("Correcto!")
        voz34 = "perfecto",pr ,"veo que estas aprendiendo"
        engine.say(voz34)
        engine.runAndWait()

    if p2 == "teclado en la pantalla" or p2 == "UN TECLADO EN LA PANTALLA":
        print("")
        print("Correcto!")
        voz35 = "perfecto",pr ,"veo que estas aprendiendo"
        engine.say(voz35)
        engine.runAndWait()

    if p2 == "teclado en pantalla" or p2 == "TECLADO EN PANTALLA":
        print("")
        print("Correcto!")
        voz36 = "perfecto",pr ,"veo que estas aprendiendo"
        engine.say(voz36)
        engine.runAndWait()




    voz30 = "haci que continuemos"
    engine.say(voz30)
    engine.runAndWait()
    voz18 = "aqi puedes ver en pantalla la combinacion control mas zeta"
    engine.say(voz18)
    engine.runAndWait()
    print("")
    print("Ctrl + Z  <--------------")
    voz19 = " la cual sirve para retroceder un paso de lo que hayas hecho ,por ejemplo si escrives en blog de notas la palabra puerta"
    engine.say(voz19)
    engine.runAndWait()
    print("--------------")
    print("|   Puerta   |")
    print("--------------")
    voz20 = "Luego ejecutas la combinacion"
    engine.say(voz20)
    engine.runAndWait()
    print("Puert  (a) <--- Se eliminan las ultimas que colocaste")
    voz21 = "y como vez se eliminara la letra haa ya que fue la ultima que colocaste"
    engine.say(voz21)
    engine.runAndWait()
    voz22 = "Esto nos ayudara bastante en los momentos que hacemos algo por error solo tenemos que ejecutar control mas zeta y retrocedera el error"
    engine.say(voz22)
    engine.runAndWait()
    
    sleep(2)
    print("Ya! , Concluimos con la version de prueba, para mas contactanos al: 829-926-8155.")
    voz37 = pr , "hasta aqi emos concluido con nuestra version de prueba, si quieres aprender mas contactanos al numero  ocho bentinueve, nueve bentiseis , ocho uno cinco cinco"
    engine.say(voz37)
    engine.runAndWait()
    voz41 = "Haci que asta luego y espero que la pases bien"
    engine.say(voz41)
    engine.runAndWait()
    print("--------------------------------------------------")
    print("|  Programa creado por: Oliver Lorenzo soriano   |")
    print("--------------------------------------------------")
    sleep(5)
    

else:
    exit()




















