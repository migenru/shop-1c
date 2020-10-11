import datetime


def save_elapsed_time(func):
    def wrap(*args, **kwargs):
        start = datetime.datetime.now()
        res = func(*args, **kwargs)
        stop = datetime.datetime.now()
        wrap.elapsed_time = stop - start
        return res

    wrap.elapsed_time = None

    return wrap



@save_elapsed_time
def concat_strings(a: str, b: str) -> str:
    return '{0} {1}'.format(a, b)

if __name__ == '__main__':
    assert concat_strings.elapsed_time == None
    assert concat_strings('a', 'b') == 'a b'
    assert concat_strings.elapsed_time > datetime.timedelta(0)