#Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def Reversed_Words(n):
    new = n.split(" ")
    new.reverse()
    m = ' '.join(new)
    return m

n = input()
print(Reversed_Words(n))