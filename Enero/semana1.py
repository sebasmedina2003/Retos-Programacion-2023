def fizzbuzz() -> None:
    for k in range(1,101):
        print('fizzbuzz' if k%3==0 and k%5 == 0 else 'fizz' if k%3 == 0 else 'buzz' if k%5 == 0 else k)

fizzbuzz()