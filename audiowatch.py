# -*- coding: utf-8 -*-
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
import time
import sqlite3
import os
import os.path
import wave
import datetime

class FileEventHandler(FileSystemEventHandler):
	def __init__(self):
		FileSystemEventHandler.__init__(self)

	def on_created(self, event):
		print("created:{0}".format(event.src_path))

		conn = sqlite3.connect(db_dir)
		cursor = conn.cursor()
		cursor.execute("delete from annotator_audio")
		cursor.execute("update sqlite_sequence set seq=0")

		for parentdir, dirname, filenames in os.walk(audio_dir):
			for filename in filenames:
				position = os.path.splitext(filename)
				if position[1] == '.wav':
					address = os.path.join(audio_dir, filename)
					WAVE = wave.open(address)
					a = WAVE.getparams().nframes
					f = WAVE.getparams().framerate
					time = a/f 
					size_B = os.path.getsize(address)
					size = str(round((size_B/1024/1024),2)) + "MB"
					timestamp = os.path.getmtime(address)
					creat_time = datetime.datetime.fromtimestamp(timestamp)
					print("Audio_address: " + address)
					print("Audio_size: " + size)
					print("Audio_length: " + str(time) + "s")
					print("Audio_name: " + position[0])
					print("Audio_format: " + position[1])
					print("Audio_create_time: " + str(creat_time))
					print("------")

					Audio_name = position[0]
					Audio_format = position[1]
					Audio_size = size
					Audio_create_time = creat_time
					Audio_length = str(time) + "s"
					Audio_address = address
					cursor.execute("insert into annotator_audio (Audio_creat_time, Audio_address, Audio_name, \ 
						Audio_des, Audio_length, Audio_size, Audio_format) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % 
						(Audio_create_time, Audio_address, Audio_name, '', Audio_length, Audio_size, Audio_format))

		cursor.close()
		conn.commit()
		conn.close()

if __name__ == "__main__":
	audio_dir = "D:\\AudioTest"
	db_dir = "D:\\Audio\\db.sqlite3"

	observer = Observer()
	event_handler = FileEventHandler()
	observer.schedule(event_handler, audio_dir, True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()
