from sys import argv

script, user_name = argv

prompt = "> "

print(f"Hi {user_name} i am You're {script}")
print("I would like to ask few questions")

print(f"Do you like me {user_name}")
likes = input(prompt)

print(f"where do your live {user_name}")
lives = input(prompt)

print(f"what kind of computer do your use")
computer = input(prompt)

print(f"""
	Alright you said {likes} about liking me
	your live in {lives} not sure where that is
	and you have a {computer} computer. Nice.


	""")
















