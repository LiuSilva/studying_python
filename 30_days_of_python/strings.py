# strings
text = "Some string, with some stuff."

text2 = "Yet, another string here."

text3 = "Concatenation combines strings like \"" + text + "\" and \"" + text2  + "\""
print(text3)
print()

# new linw
text = 'Often\nYou need a new line'
print(text)
print()

# tab
text = 'Often a \t tab is needed.'
print(text)
print()

# escaped quotes
text = 'Sometimes it\'s your quote sometimes it isn\'t'
print(text)

text = "Sometimes it\'s a \"Quote from someone else\""
print(text)
print()

# escaped linebreak
text = "Sometimes you need to have \
a inline break that isn't a linebreak."
print(text)
print()

# lower case
text = "Some string, with some stuff."
text.lower()
print(text)
print()

# upper case
text = "Some string, with some stuff."
text.upper()
print(text)
print()

# capitalize
lower_cased = "this sentence needs to be capitalized."

cap_string = lower_cased[0].upper() + lower_cased[1:]
print(cap_string)
print()

# break strings
text = "Some string, with some stuff."
print(text.split())
print()

# lenght
text_length = len("Some string, with some stuff.")
print(text_length)
print()

# Using  keywords arguments
text = "This is {variable_a} formatted string".format(variable_a="variable based")
print(text)
print()

text = "This is another {variable_a} formatted string with \
multiple variables like {a} {b} {c}.".format(
    variable_a="variable based", 
    a="some random", b="replacement", c="text")
print(text)
print()

text = """So, {name}, the best part is formated strings you don't have to order it. 
And these keyword argument replacements, ({var_a}, {var_b}, {name}) can be reused over and over.
Seriously {name}, this is some fun formatting.""".format(
            name="Jerry", 
            var_a="Variable 1", 
            var_b="Variable 2")
print(text)
print()

# using arguments
text = "This is {0} formatted string".format("argument based")
print(text)
print()

text = "This is another {0} formatted string \
with multiple variables like {1} {2} {3}.".format(
    "variable based", 
    "some random", 
    "replacement", 
    "text"
    )
print(text)
print()

text = """So, {0}, the best part is formated strings you don't have to order it. 
And these argument replacements, ({1}, {2}, {0}) can be reused over and over.
Seriously {0}, this is some fun formatting.""".format(
            "Jerry", 
            "Variable 1", 
            "Variable 2")
print(text)
print()

# substitution
text = "This is %s formatted string" %("replacement")
print(text)

text = "The %%s format string is not as %s, but still very %s." %("robust", "useful")
print(text)
print()

# float substitution
text = "0 decimal places: %.0f" %(20)
print(text)
print()

text = "2 decimal places: %.2f" %(20)
print(text)
print()

text = "10 decimal places: %.10f" %(20)
print(text)
print()

text = "400 decimal places: %.400f" %(20)
print(text)
print("\n")


import datetime
today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)

text = today.strftime('%-m/%-d/%y')
print(text)

now = datetime.datetime.utcnow() #utc time
text = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(text)

now = datetime.datetime.now() #local time
date_text = now.strftime('%Y/%m/%d %H:%M:%S.%f') #[:-3]
text = "Time is: %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%B %d, %Y %H:%M:%S.%f %p')
text = "Time is %s" %(date_text)
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%x')
text = "Time is %s" %(date_text)
print(text)