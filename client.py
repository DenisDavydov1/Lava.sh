from telethon import TelegramClient, sync, events
import random
import time
import threading
import asyncio
import utils

# start client with config file
params = utils.Params()
params.start_client()
print("Client runs...")

# set target users to respond
params.convert_str_targets_to_id()
params.set_targets_usernames()

# send message to target user
async def send_next_message(target_index, message_obj):
	global params
	target_id = params.targets[target_index]
	target_username = params.targets_usernames[target_index]
	message_text = params.get_message_to_send(target_index)
	await params.client.send_message(target_id, message_text)
	print("[msg_id: {0:d}] Response \"{1:s}\" sent to \"{2:s}\" ({3:d})".format(
		message_obj.id, message_text, target_username, target_id))

# conditions for aborting response
def abort_response(target_index, message_obj):
	global params

	# if the message is already manually read
	# to do later ...

	# if the message is the last in chat
	if (message_obj.id != params.last_message_id[target_index]):
		print("[msg_id: {0:d}] But it is not the last".format(message_obj.id))
		return True
	return False

# newly received message event
@params.client.on(events.NewMessage(chats=tuple(params.targets)))
async def normal_handler(event):
	global params
	for i in range(len(params.targets)):
		# set message metas
		cur_user_id = event.message.peer_id.user_id
		cur_msg_id = event.message.id
		if (cur_user_id == params.targets[i] and
			event.message.out == False and
			event.message.media != None and
			event.message.sticker == None):
			# remember the last received message
			params.last_message_id[i] = cur_msg_id
			print("[msg_id: {0:d}] New meme received from \"{1:s}\" ({2:d})".format(
				cur_msg_id, params.targets_usernames[i], cur_user_id))
			# сheck for abort
			if abort_response(i, event.message) == True: return
			# check for nite mode
			if (params.is_night() == True):
				print("[msg_id: {0:d}] It is night. Sleeping...".format(cur_msg_id))
				while (params.is_night() == True):
					await asyncio.sleep(60)
			# wait randomized time before sending response
			await asyncio.sleep(random.randint(
				params.response_delay[0], params.response_delay[1]))
			# check for abort
			if abort_response(i, event.message) == True: return
			# finally sending the message
			await event.message.mark_read()
			await send_next_message(i, event.message)
			break

# run client in loop
params.client.run_until_disconnected()
print("Client stops.")
