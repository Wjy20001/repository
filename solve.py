# GEO1000 - Assignment 1
# Authors:Jiaoyang Wu
# Studentnumbers:5902762

from math import sqrt


def abc(a, b, c):
    dis = discriminant(a, b, c)
    if dis > 0:
        x1 = (-b - sqrt(dis)) / (2 * a)
        x2 = (-b + sqrt(dis)) / (2 * a)
        print('The roots of '+str(a)+' x^2 + '+str(b)+' x + '+str(c)+' are:')
        print('x1 = ' + str(x1) + " ," + 'x2 = ' + str(x2))
    elif dis == 0:
        x = (-b - sqrt(dis)) / (2 * a)
        print('The roots of '+str(a)+' x^2 + '+str(b)+' x + '+str(c)+' are:')
        print('x = ' + str(x))
    else:
        print('The roots of '+str(a)+' x^2 + '+str(b)+' x + '+str(c)+' are:')
        print('not real')


def discriminant(a, b, c):
    dis = b ** 2 - 4 * a * c
    return dis


# test
abc(2.0, 0.0, 0.0)
abc(1.0, 3.0, 2.0)
abc(3.0, 4.5, 9.0)