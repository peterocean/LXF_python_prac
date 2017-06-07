# -*- coding:utf-8 -*-

height = 1.75
weight = 80.5
bmi = weight/(height*height)

if bmi < 18.5:
    print u'过轻'
elif bmi <= 25:
    print u'正常'
elif bmi <= 32:
    print u'肥胖'
else:
    print u'严重肥胖'

