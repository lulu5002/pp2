import time
import math

def square_root_with_delay(num, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(num)

num = int(input())
delay_ms = int(input())

result = square_root_with_delay(num, delay_ms)

print(f"Square root of {num} after {delay_ms} milliseconds is {result}")