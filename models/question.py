class Question:
	def __init__(self, prompt, name:str, max_tokens=1000, ):
		self.name = name
		self.max_tokens = int(max_tokens)
		self.prompt = prompt

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name
