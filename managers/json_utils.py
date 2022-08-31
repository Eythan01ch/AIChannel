import json


class JsonManager:
	""" This class is used to manage JSON files"""

	def __init__(self, path):
		self.json_path = path
		try:
			with open(self.json_path):
				pass
		except FileNotFoundError:
			with open(self.json_path, 'x') as jp:
				json.dump([], jp)

	def return_json_obj_read(self):
		"""
		It opens the json file, reads it, and returns the json object
		:return: The json object is being returned.
		"""
		with open(self.json_path, 'r') as json_file:
			return json.load(json_file)

	def update_json(self, json_dict):
		"""
		This function takes a dictionary and updates the json file with the dictionary

		:param json_dict: The dictionary you want to update the json file with
		:type json_dict: dict
		"""
		json_obj = self.return_json_obj_read()
		json_obj.append(json_dict)

		with open(self.json_path, 'w') as json_file:
			json.dump(json_obj, json_file)

		return self.return_json_obj_read()

