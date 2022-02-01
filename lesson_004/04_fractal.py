# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1000, 1000
import random


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def draw_branches(s_point, length, angle):
    if length < 4:
        return
    # print(length)
    angle_1 = angle - 30
    v1 = sd.get_vector(start_point=s_point, angle=angle_1, length=length)
    v1.draw()
    angle_2 = angle + 30
    v2 = sd.get_vector(start_point=s_point, angle=angle_2, length=length)
    v2.draw()
    start_v1 = v1.end_point
    start_v2 = v2.end_point
    _length = length * .75
    _angle1 = angle - sd.random_number(10, 60)
    _angle2 = angle - sd.random_number(-60, 10)
    draw_branches(s_point=start_v1, length=_length, angle=_angle1)
    draw_branches(s_point=start_v2, length=_length, angle=_angle2)


x, y = 300, 100
st_point = sd.get_point(x, y)
_length = 150
_width = 3
_angle = 90

draw_branches(s_point=st_point, length=_length, angle=_angle)

# 4) Усложненное задание (делать по желанию)


# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
sd.random_number()

sd.pause()