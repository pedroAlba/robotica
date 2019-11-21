#Autor: Simon Monk
 
import RPi.GPIO as GPIO
import time
 
pan_pin = 18
tilt_pin = 16
 
#Ajuste estes valores para obter o intervalo completo do movimento do servo
deg_0_pulse   = 0.5 
deg_180_pulse = 2.5
f = 50.0
 
# Faca alguns calculos dos parametros da largura do pulso
period = 1000/f
k      = 100/period
deg_0_duty = deg_0_pulse*k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k
 
#Iniciar o pino gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(pan_pin, GPIO.OUT)
GPIO.setup(tilt_pin, GPIO.OUT)
pan_pwm = GPIO.PWM(pan_pin,f)
tilt_pwm = GPIO.PWM(tilt_pin,f)
pan_pwm.start(0)
tilt_pwm.start(0)

 

def move(pan, tilt):
        pan_processed = deg_0_duty + (pan/180.0)* duty_range
        pan_pwm.ChangeDutyCycle(pan_processed)

        tilt_processed = deg_0_duty + (tilt/180.0)* duty_range
        tilt_pwm.ChangeDutyCycle(tilt_processed)
