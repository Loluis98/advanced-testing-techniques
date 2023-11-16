def addthis(*args):
    try:
        return sum(args)
    except (TypeError, Exception) as e:
        return f'Wrong type error passed in {e}'

print(addthis(1,2,'twenty',123))
