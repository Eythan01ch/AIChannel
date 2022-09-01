from models.question import Question


class QuestionsPool:
	"""
	The QuestionsPool class is a class that contains
	a list of questions that are related to a subject
	"""

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
		self.list_of_topics_related_question = Question(
			prompt=f'give me a list of related topics about {self.subject}',
			name='TOPICS_RELATED',
			max_tokens=500,
		)
		self.simple_explanation = Question(
			prompt=f'explain {self.subject} in the most simple way',
			name='SIMPLE_EXPLANATION',
			max_tokens=500,
		)

		self.questions_pool = [
			self.description_question,
			self.term_question,
			self.list_of_topics_related_question,
			self.simple_explanation,
		]

	def __str__(self):
		return str(self.questions_pool)
