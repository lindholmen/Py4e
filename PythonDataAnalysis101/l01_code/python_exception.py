import traceback

try:
    print('try...')
    r = 10 / 0
except ZeroDivisionError as e:
# 2.7: except ZeroDivisionError, e:
    print('ZeroDivisionError:', e)
    print(traceback.print_exc())
finally:
    print('finally...')