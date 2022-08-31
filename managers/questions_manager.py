from managers.questions_pool import QuestionsPool
from models.question import Question



class QuestionsManager(QuestionsPool):
	def __init__(self, subject):
		super(QuestionsManager, self).__init__(subject)
		while True:
			print(self.questions_pool)
			more_q = input("Would you like to add more questions for the subject?| Y for yes\n").lower().strip()
			if more_q in ['yes', 'y', 'yy']:
				self.create_question()
				print(f'added question {self.questions_pool[-1]}')
				print(self.questions_pool)
			else:
				sure = self._are_you_sure()
				if sure:
					break
				else:
					continue

	def create_question(self):
		"""
		It takes a prompt, name, and max_tokens as input, and creates a new Question object with those attributes
		:return: A question object
		"""
		prompt = input('Prompt of the question? \n(should include "{0}" for the subject placeholder)\n').format(
			self.subject)
		name = input('Name? \njust the way the question is represented\n').upper()
		max_tokens = input('max_tokens? \nfor openai 100-3000\n')
		if not max_tokens.isdigit():
			max_tokens = 1000
		else:
			max_tokens = int(max_tokens)

		q = Question(
			prompt=prompt,
			name=name,
			max_tokens=max_tokens,
		)
		self.questions_pool.append(q)
		return q

	def _are_you_sure(self):
		print(self.questions_pool)
		sure = input('are you sure you want to stop adding questions? | YES for yes | NO for no\n').strip().lower()
		if sure == 'yes':
			return True
		elif sure == 'no':
			return False

