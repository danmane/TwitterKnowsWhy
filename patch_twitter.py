import twitter
from pretty_time import prettyITime

TwitterStatus = twitter.Status

class Status(TwitterStatus):
	def __init__(self, *args, **kwargs):
		TwitterStatus.__init__(self, *args, **kwargs)
		self.args = args
		# self.time = parseTime(self.created_at)
		self.pretty_time = prettyITime(self.created_at_in_seconds)
		self.text = self.text.encode('utf-8', 'ignore')
		self.is_retweet = self.text[0:3] == "RT "
		self.phrase = None

	def __str__(self):
		return self.pretty_time + ": " + (self.phrase or self.text)
		
twitter.Status = Status