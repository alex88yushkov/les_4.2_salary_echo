# Exercise #1
def show_employee(name = "Trus", sal = 5000):
    name = "Name: " + name
    sal = "Salary: " + str(sal)

    print(name, sal, sep=", ")

show_employee()
show_employee(name = 'Balbes')
show_employee(name = 'Bivaliy', sal = 4000)

# Exercise #2
# VARIANT 1:
#Define shout_echo
def shout_echo(word1 = "Hey ", echo = 1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo()

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo(echo = 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)

# VARIANT 2:
def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey ")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey ", 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)

