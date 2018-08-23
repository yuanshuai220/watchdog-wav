# watchdog-wav
Code for using watchdog python package to monitor the file system and adding wavefile attributes to the sqlite database.

# Requirement
- Anaconda 3
- watchdog 0.8.3

# Datebase Structure
Table Name: annotator_audio
| Field | Attributes |
| ------ | ------ |
| Audio_id | AutoField(primary_key=True) |
| Audio_creat_time | DateTimeField(auto_now_add=True) |
| Audio_address | CharField(max_length=30) |
| Audio_name | CharField(max_length=30) |
| Audio_des | CharField(max_length=30) |
| Audio_length | CharField(max_length=30) |
| Audio_size | CharField(max_length=30) |
| Audio_format | CharField(max_length=30) |
