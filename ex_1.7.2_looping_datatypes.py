# 1.dict: Looping through dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# ----------------------------------------------------
# 2.list: Looping through list using enumerate() function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 2.1.list: combining two list using zip() function 
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 2.2.list:  looping through list by sorting and filtering unique items
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# ----------------------------------------------------
#3. range: Looping through range in reverse order
for i in reversed(range(1, 10, 2)):
    print(i)
