def sandwich(*items):
    print('Give me a sandwich with the following toppings:')
    for item in items:
        print(f'· {item}')

sandwich('roasted beef')

sandwich('cheese', 'lettuce', 'tomato')

sandwich('bacon', 'egg', 'hashbrown')