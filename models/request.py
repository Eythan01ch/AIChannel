import os

import openai

from managers.json_utils import JsonManager


class Request:
	def __init__(self, question, model, temperature):

		self.log_json_manager = JsonManager('log_requests.json')
		self.prompt = question.prompt
		self.temperature = temperature
		self.model = model
		self.max_tokens = question.max_tokens



	def make_request(self):
		"""
		The function makes a request to the OpenAI API to generate a completion for the prompt
		"""
		openai.api_key = os.getenv('OPENAI_API_KEY')
		response = openai.Completion.create(
			model=self.model,
			prompt=self.prompt,
			max_tokens=self.max_tokens,
			temperature=self.temperature,
		)
		self.save_response_log(response)
		return response

	def save_response_log(self, response):
		"""
		It updates the json file with the response.

		:param response: The response object returned by the request
		"""
		self.log_json_manager.update_json(response)

	def get_text(self, response):
		return response.get('choices')[0].get('text')



