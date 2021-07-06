import os
import _thread as thread

counter = 0

#NOTE: THIS IS VERY ILEGAL AND I AM NOT RESPOINSIBLE FOR WHAT YOU DO WITH THIS CODE
def ping(ip,times,delay):
    os.system("ping " + ip + " -n " + str(times) + " -w " + delay)
    print("you going to jail boi")

print("NOTE: THIS IS VERY ILEGAL AND I AM NOT RESPOINSIBLE FOR WHAT YOU DO WITH THIS CODE. THIS IS FOR EDUCATIONA PURPOSES ONLY")
ip = input("What ip do you want to ping? ")
times = int(input("how many times do you want to ping the it? "))
delay = input("What delay would you want to put on it? 0 for none ")

while times > counter:
    thread.start_new_thread(ping(ip,times,delay),0)
    counter = counter + 1
