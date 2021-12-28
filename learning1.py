print("Hello,World")
print("Allahuakbar-\nAllah is great")
print(2<18<20)
print("The itsy bitsy spider", "climebed up" ,"waterspout")
print("My name is", "Python.")
print("Monty Python.")
print("Learining keyword argument")
#learning keyword arguments of print()
#end=" "
#
print("My anme is", "S M Faizan Alam",end="\n")
#The default behavior reflects the situation where the end
#keyword argument is implicitly used in the following way: end="\n"
print("My name is ", end="")
print("Monty Python.")
#The keyword argument that can do this is named sep (like separator).
print("My", "name", "is", "Monty", "Python.", sep="-")
#Both keyword arguments may be mixed in one invocation,
#just like here in the editor window.
#The example doesn't make much sense, but it visibly presents
#the interactions between end and sep.
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Programming","Essentials","in",sep="***",end="...")
print("Python")


