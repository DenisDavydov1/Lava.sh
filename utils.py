import json
from datetime import datetime
from telethon import TelegramClient, sync, events
import random
import requests

########### configuration files and links ############
config_file_path = "config.json"
messages_to_send_jsonblob = "location-here"
######################################################

class Params:
	# create instance from config json file
	def __init__(self):
		vars(self).update(self.load_json_obj(config_file_path))
		self.last_message_id = [0 for target in self.targets]

	# run telegram client
	def start_client(self):
		self.client = TelegramClient(self.session_name, self.client_api_id, self.client_api_hash)
		self.client.start()

	# get target users ids
	def convert_str_targets_to_id(self):
		for i in range(len(self.targets)):
			if type(self.targets[i]) == str:
				self.targets[i] = self.get_user_id_by_username(self.targets[i])

	# get target users usernames
	def set_targets_usernames(self):
		self.targets_usernames = [self.get_username_by_user_id(
			target) for target in self.targets]

	# get username by user_id
	def get_username_by_user_id(self, user_id):
		for dialog in self.client.iter_dialogs():
			if (dialog.id == user_id):
				return dialog.title

	# get user_id by username
	def get_user_id_by_username(self, username):
		for dialog in self.client.iter_dialogs():
			if (dialog.title == username):
				return dialog.id

	# get next message to send from jsonblob and put updated list back
	def get_message_to_send(self, target_index):
		messages_to_send_json = JsonBlobHandler.GetJsonBlob()
		messages_to_send = messages_to_send_json["messages_to_send"]

		while len(messages_to_send) <= target_index:
			messages_to_send.append([])

		if len(messages_to_send[target_index]) == 0:
			messages_to_send[target_index] = random.sample(self.messages, len(self.messages))
		message = messages_to_send[target_index].pop(0)

		messages_to_send_json["messages_to_send"] = messages_to_send
		JsonBlobHandler.PutJsonBlob(messages_to_send_json)
		return message

	# get json dict from file
	def load_json_obj(self, filepath):
		try:
			with open(filepath, 'r', encoding="utf-8") as f:
				return json.load(f)
		except:
			print("file error:", filepath)
			exit(1)

	# write json dict to file
	def dump_json_obj(self, filepath, json_object):
		try:
			with open(filepath, 'w') as f:
				json.dump(json_object,
						f,
						sort_keys=False,
						indent=4,
						ensure_ascii=False,
						separators=(",", ": "))
		except:
			print("file error:", filepath)
			exit(1)

	# check for sleep time
	def is_night(self):
		hour = datetime.now().hour
		if self.sleep_time[0] <= self.sleep_time[1]:
			return self.sleep_time[0] <= hour <= self.sleep_time[1]
		else:
			return not self.sleep_time[1] < hour < self.sleep_time[0]

class JsonBlobHandler:
	# get request to jsonblob server
	def GetJsonBlob():
		global messages_to_send_jsonblob
		response = requests.get(messages_to_send_jsonblob)
		if response.status_code == 200:
			return json.loads(response.content)
		else:
			print("[JsonBlob] Error in GET request")
			exit(1)

	# put request to jsonblob server
	def PutJsonBlob(json_obj):
		global messages_to_send_jsonblob
		response = requests.put(
			url=messages_to_send_jsonblob,
			data=json.dumps(json_obj),
			headers={
				'Content-Type': 'application/json',
				'Accept': 'application/json'})
		if response.status_code != 200:
			print("[JsonBlob] Error in PUT request")
			exit(1)
