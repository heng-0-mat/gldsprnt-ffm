# -*- coding: utf-8 -*-
# !/usr/bin/python

from classes import helpers
import threading
import parallel

class BikeObserverX86():

    def __init__(self, parport, parfunc):

        self.counter = 0
        self.parport = parport
        self.parfunc = parfunc
        self.stop_thread = False

        #print(f"init {self.parfunc}")
        self.sensor_thread = threading.Thread(target=self.read_sensor, args=())
        self.sensor_thread.start()


    def count_up(self):
        self.counter += 1

    def start_listening(self):
        self.counter = 0
        self.sensor_thread = threading.Thread(target=self.read_sensor, args=())
        self.sensor_thread.start()

    def stop_listening(self):
        self.stop_thread = True
        #self.sensor_thread.join()

    def read_count(self):
        result = self.counter
        self.counter = 0
        return result

    # worker function for thread
    def read_sensor(self):

        sensor_func = getattr(self.parport, self.parfunc)

        last_state = True # when signal is received state turns to False
        while(self.stop_thread == False):
            state = sensor_func()
            if (state == False and last_state == True):
                self.count_up()
                #print(f"{self.sensor_thread.name} - {self.parfunc}: {self.counter}")
            last_state = state
