#!/usr/bin/env python
import pylast
import sys
from datetime import datetime

API_KEY="cf7dc8bd12a610a8209ab98bdfa773b4"


def get_date(track):
	"""
	Given a track, return the DateTime object
	"""
	return datetime.fromtimestamp(long(track.timestamp))

def get_delta(date):
	"""
	Given a date, how many seconds/minutes/hours have passed (STRING)
	"""
	now = datetime.now()
	delta = (now - date)
	if delta.seconds / 60 / 60:
		return str(delta.seconds / 60 / 60) + " hours ago"
	if delta.seconds / 60:
		return str(delta.seconds / 60) + " minutes ago"
	if delta.seconds:
		return str(delta.seconds) + " seconds ago"
	else:
		return "???"

def get_network(api=API_KEY):
	"""
	Return LastFM Network Object using api provided
	"""
	network = pylast.LastFMNetwork(api_key=api)
	return network


def currently_playing(username):
	"""
	Given a username, return the current song they're listening to
	"""
	network = get_network()
	user = network.get_user(username)
	try:
		return user.get_now_playing()
	except:
		print("User %s does not exist" % username)	
		sys.exit(1)


def last_played(username):
	"""
	Given a username, return the last song they listened to
	"""
	network = get_network()
	user = network.get_user(username)
	try:
		recent = user.get_recent_tracks()
		if recent:
			return recent[0]
		else:
			return None
	except:
		print("User %s does not exist" % username)	
		sys.exit(1)


def print_track(track, prefix, suffix=""):
	"""
	Given a track and a message, print the message as well as the track details
	"""
	print("%s %s - %s %s" % (
		prefix,
		track.get_title(),
		track.get_artist().get_name(),
		suffix
	))


if __name__ == "__main__":
	"""
	Main entry point, arguments are:
		username	|	LastFM user
		message		|	Custom message prefix (optional)
	"""
	username = sys.argv[1]
	if len(sys.argv) > 2:
		message = " ".join(sys.argv[2:])
	else:
		message = "Listening To:"

	playing = currently_playing(username)
	if playing:
		print_track(playing, message)
	else:
		last_track = last_played(username)
		if last_track:
			print_track(last_track.track, "Last Played:", "[" + get_delta(get_date(last_track)) + "]")
		else:
			print("User %s has no recent tracks" % username)
