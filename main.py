name: str = input('Enter a name:  ')
age: str = input('Enter a age:  ')
gender: str = input('Enter a gender: ')
state: str = input('Enter a state of origin:  ')
food: str = input('Enter your faviourite food:  ')


story: str = f"""
______________________________________________________
Hi, i'm {name} , {age} years old, a {gender},
i'm from {state} state ,
which am proud to be from,
my favourite food is {food}.
THANKYOU.
________________________________________________________"""

print(story)
