# -*- coding: utf-8 -*-
# !/usr/bin/python

from pygame import Surface


class MenuItem():

    def __init__(self, item, font, font_color, (pos_x, pos_y)=(0, 0)):
        self.item = item
        self.base_text = item["text"]
        self.text = item["text"]
        self.incrementable = False

        if "increment" in self.item:
            self.incrementable = True
            self.increment_min = self.item["increment"]["min"]
            self.increment_max = self.item["increment"]["max"]
            self.increment_value = self.item["increment"]["value"]

            self.increment_format = "%s:%d"
            if "format" in self.item["increment"]:
                self.increment_format = self.item["increment"]["format"]

            self.increment_step = 1
            if "step" in self.item["increment"]:
                self.increment_step = self.item["increment"]["step"]

            self.set_increment(self.increment_value)

        self.value = 0
        self.font = font
        self.label_text = self.font.render(self.text, 1, font_color)
        self.label = self.create_label((255, 255, 255), (0, 0, 0))
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.prev_position = self.position

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, color):
        self.label_text = self.font.render(self.text, 1, color)

    def set_active_state(self):
        self.label = self.create_label((68, 68, 68), (255, 255, 255))

    def set_default_state(self):
        self.label = self.create_label((255, 255, 255), (68, 68, 68))

    def set_text(self, text):
        self.text = text

    def set_increment(self, value):
        self.increment_value = max(self.increment_min, min(value, self.increment_max))
        self.set_text(self.increment_format % (self.base_text, self.increment_value))

    def increment(self):
        self.set_increment(self.increment_value + self.increment_step)

    def decrement(self):
        self.set_increment(self.increment_value - self.increment_step)

    def create_label(self, font_color, box_color):
        label_box = Surface((self.label_text.get_rect().width + 40, self.label_text.get_rect().height + 10))
        label_box.fill(box_color)
        self.set_font_color(font_color)
        label_box.blit(self.label_text, (20, 5))
        return label_box