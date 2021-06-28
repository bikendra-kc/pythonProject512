'''5 Write a function calledshow_stars(rows).If rows is
5, it should print thefollowing:***************.'''
def called_stars(rows):
    j = "*****"
    for i in range(1,rows+1):
        print('*'*i)


called_stars(5)