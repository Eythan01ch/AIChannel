import json

from managers.file_creator import FileCreator


class Script(FileCreator):

	def __init__(self, subject):
		super(Script, self).__init__(subject)
		self.start_of_script = "This is the beginning of the script"
		self.end_of_script = "This is the end of the script"

	def write_paragraph(self, paragraph):
		with open(self.script_path, 'a') as script_file:
			script_file.write(paragraph)

	def write_json(self, texts):
		with open(self.texts_path, 'w') as json_file:
			json.dump(texts, json_file)


	def create_script(self, texts):


		self.write_paragraph(self.start_of_script)
		for name, values in texts.items():
			paragraph = f'\n\n{name}\n\n{values.get("prompt")}{values.get("answer")}'
			self.write_paragraph(paragraph)

		self.write_paragraph(self.end_of_script)
		self.write_json(texts)
