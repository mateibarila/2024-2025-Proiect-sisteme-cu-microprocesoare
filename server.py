import network
import socket
import time
from machine import Pin
onboard_led = Pin("LED", Pin.OUT)
buzzer = Pin(14, Pin.OUT)  
led_rosu = Pin(13, Pin.OUT)
led_galben = Pin(15, Pin.OUT)
PIN_TRIGGER = machine.Pin(11, machine.Pin.OUT)
PIN_ECHO = machine.Pin(12, machine.Pin.IN)
PIN_TRIGGER.value(0)
time.sleep(2)
prag_cm1=0
prag_cm2=0
mod_automat_flag=False
led_rosu.off()
led_galben.off()
buzzer.off()
import time
from machine import Pin

def citeste_distanta(timeout_us=50000):  
    PIN_TRIGGER.value(0)
    time.sleep_us(2)
    PIN_TRIGGER.value(1)
    time.sleep_us(10)
    PIN_TRIGGER.value(0)
    start = time.ticks_us()
    while PIN_ECHO.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > timeout_us:
            print("Timeout waiting for echo HIGH")
            return -1
    pulse_start = time.ticks_us()
    while PIN_ECHO.value() == 1:
        if time.ticks_diff(time.ticks_us(), pulse_start) > timeout_us:
            print("Timeout waiting for echo LOW")
            return -1
    pulse_end = time.ticks_us()
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance_cm = pulse_duration * 0.0343 / 2  
    return distance_cm

def mod_automat(prag_cm1,prag_cm2):
    while mod_automat_flag:
        print("mod_automat")
        dist = citeste_distanta()
        print("Distanta:", dist, "cm")
        if dist < prag_cm1:
            led_rosu.on()
            led_galben.off()
            buzzer.on()
        elif dist>=prag_cm1 and dist<prag_cm2:
            led_rosu.off()
            led_galben.on()
            buzzer.on()
        else:
            led_rosu.off()
            led_galben.off()
            buzzer.off()
        time.sleep(1)
                
def mod_manual(comanda):
    if comanda == "on":
        led_rosu.on()
        buzzer.on()
    elif comanda == "off":
        led_rosu.off()
        buzzer.off()

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='PicoW_AP', security=0)
print(ap.ifconfig())
html = """<!DOCTYPE html>
<html>
    <head> <title>Pico W</title> </head>
    <body> <h1>Pico W</h1>
        <p>%s</p>
        <form method="POST" action="/mod_automat">
            <label for="rosu">Prag led rosu:</label>
            <input type="text" id="rosu" name="rosu" value="%s"><br>
            <label for="galben">Prag led galben:</label>
            <input type="text" id="galben" name="galben" value="%s"><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
print('Listening on', addr)
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        if '/manual/on' in request:
            mod_manual("on")
            prag_cm1=0
            prag_cm2=0
        if '/manual/off' in request:
            mod_manual("off")
            prag_cm1=0
            prag_cm2=0
        if mod_automat_flag==False:
            request = request.decode()
            stateis = ""
            rosu_value="0"
            galben_value="0"
            if "POST" in request:
                post_index = request.find("\r\n\r\n")
                if post_index != -1:
                    post_data = request[post_index + 4:]
                    params = {}
                    pairs = post_data.split('&')
                    for pair in pairs:
                        if '=' in pair:
                            key, value = pair.split('=', 1)
                            key = key.replace('+', ' ')
                            value = value.replace('+', ' ')
                            params[key] = value
                    rosu_value = params.get('rosu', '0')
                    galben_value = params.get('galben', '0')
                    try:
                        print("Prag LED rosu:", int(rosu_value))
                        prag_cm1=int(rosu_value)
                        print("Prag LED galben:", int(galben_value))
                        prag_cm2=int(galben_value)
                    except ValueError:
                        print("Valoare/valori invalide")
            led_on = request.find('/light/on')
            led_off = request.find('/light/off')
            if "/favicon.ico" in request:
                cl.close()
                continue
        print(prag_cm1)
        print(prag_cm2)
        if prag_cm1!=0 and prag_cm2!=0:
            try:
                mod_automat_flag=True
                mod_automat(prag_cm1, prag_cm2)
            except ValueError:
                print("Valoare/valori invalide")
        response = html % (stateis, rosu_value, galben_value)
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n'+response)
        cl.close()
    except OSError as e:
        cl.close()
        print('Connection closed')