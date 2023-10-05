import time

def get_time_track(precision):
    def time_track(func):
        def surrogate(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            rounded_time = round((ended_at - started_at), precision)
            print(f'Function completed in {rounded_time} second(s)')
            return result
        return surrogate
    return time_track


@get_time_track(precision=6)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))



result = digits(1235, 8234, 8325, 9213)
print(result)
