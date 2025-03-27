# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. 
# We might check their age and return different things depending on how old they are!

ADULT_AGE = 18  

def is_adult(age):
    return age >= ADULT_AGE

# Taking user input
age = int(input("How old is this person?: "))
print(is_adult(age))

