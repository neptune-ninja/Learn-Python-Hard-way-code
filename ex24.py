print("Let's practive everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t for tabs.')

poem = """
\t The lovely world
with logic so firmly plancted 
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none."""

print("..................")
print(poem)
print("..................")

five = 10 - 2 + 3 - 6
print(f"This should be five :{five}")


def secret_formula(started):
	jeyy_beans = started*500
	jars = jeyy_beans/1000
	crates = jars/100
	return jeyy_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print("With a start point of {}".format(start_point))

print(f"we have {beans} beans , {jars} jars and {crates} crates .")

start_point = start_point/10

print("we can also do this way:")

formula = secret_formula(start_point)

print("we would have {} Beans, {} jars and {} crates.".format(*formula))













