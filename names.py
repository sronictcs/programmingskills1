name = "alan turing"
##To change case of string use variable.upper() and variable.lower()
print(name.upper())
print(name.lower())

first_name = "alan"
last_name = "turing"

#using f-strings to format a string - replaces the variables in braces with its values.
full_name = f"{first_name} {last_name}"
print(full_name)

#string.title() makes string title case
print(f"Hello, {full_name.title()}!")

#f-string as variable called by print
message = f"Hello, {first_name} {last_name}"
print(message)



