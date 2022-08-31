from managers.questions_manager import QuestionsManager
from models.request import Request
from models.script import Script


class RequestsManager:

	def __init__(self, model="text-davinci-002", temperature=0.4):
		self.subject = input("What is The Subject of the video? \n").lower()
		self.temperature = temperature
		self.model = model
		self.questions_manager = QuestionsManager(self.subject)

		self.texts = {}

		for question in self.questions_manager.questions_pool:
			print('Making a request with prompt %s' % question.prompt)
			request = Request(
				model=self.model,
				temperature=self.temperature,
				question=question
			)
			response = request.make_request()

			self.texts.update(
				{
					question.name: {
						'prompt': question.prompt,
						'answer': request.get_text(response)
					}
				}
			)


		script_creator = Script(self.subject)
		script_creator.create_script(texts=self.texts)
