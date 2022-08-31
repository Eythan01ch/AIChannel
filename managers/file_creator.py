import json
import os


class FileCreator:

	def __init__(self, subject):
		self.parent_dir = "scripts"

		self.base_path = os.path.join(self.parent_dir, subject)



		self.script_path = os.path.join(self.base_path, f'script_about_{subject}.text')
		self.texts_path = os.path.join(self.base_path, f'text_for_{subject}.json')

		self.create_files()

	def create_files(self):
		os.mkdir(self.base_path)

		with open(self.script_path, 'x'):
			pass
		with open(self.texts_path, 'w') as texts_file:
			json.dump({}, texts_file)


