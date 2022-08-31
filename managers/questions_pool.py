from models.question import Question


class QuestionsPool:
	def __init__(self, subject):
		self.subject = subject
		self.description_question = Question(
			prompt=f'give me a detailed description of the {self.subject}',
			name='DESCRIPTION',
			max_tokens=3000
		)
		self.term_question = Question(
			prompt=f'where does the term {self.subject} come from?',
			name='ORIGIN_OF_TERM',
			max_tokens=500,
		)

		self.questions_pool = [self.description_question, self.term_question]

	def __str__(self):
		return str(self.questions_pool)