from manim_data_structures import *
from manim import *

import os
import shutil

class ArrayBug1(Scene):
    def construct(self):
        arr = MArray(self, [0] * 3 + [1] * 4, label="Array A", mob_arr_label_args={'color': BLACK}).align_on_border(LEFT)
        self.add(arr)

class ArrayBug2(Scene):
    def construct(self):
        arr = MArray(self, [0] * 3 + [1] * 4, label="Array A", mob_arr_label_args={'color': BLACK}).align_on_border(LEFT)

        pi = MArrayPointer(self, arr, 4, "i")
        pj = MArrayPointer(self, arr, 1, "j")

        self.add(pi, pj)
        self.add(arr)


class ArrayBug3(Scene):
    def construct(self):
        arr = MArray(self, [0] * 2 + ['?'] * 3 + [1] * 4, label="Array A", mob_arr_label_args={'color': BLACK}).align_on_border(LEFT)
        pi = MArrayPointer(self, arr, 3, "i")
        self.add(pi, arr)


if __name__ == "__main__":
    os.system("manim -s -t -r 500,150  array.py ArrayBug1")
    shutil.copyfile('media/images/array/ArrayBug1_ManimCE_v0.17.2.png', 'array-bug-1.png')

    os.system("manim -s -t -r 400,200  array.py ArrayBug2")
    shutil.copyfile('media/images/array/ArrayBug2_ManimCE_v0.17.2.png', 'array-bug-2.png')

    os.system("manim -s -t -r 700,200  array.py ArrayBug3")
    shutil.copyfile('media/images/array/ArrayBug3_ManimCE_v0.17.2.png', 'array-bug-3.png')

