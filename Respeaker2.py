import RPi.GPIO as GPIO

from core.base.model.AliceSkill import AliceSkill


class Respeaker2(AliceSkill):
	"""
	Author: Psychokiller1888
	Description: Let's you configure the gpio button available on the device
	"""

	GPIO_PIN = 17

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		super().__init__()


	def onStart(self):
		super().onStart()
		GPIO.add_event_detect(self.GPIO_PIN, GPIO.FALLING, callback=self.onButton, bouncetime=300)


	def onStop(self):
		super().onStop()
		GPIO.remove_event_detect(self.GPIO_PIN)


	def onButton(self, _channel: int):
		action = self.getConfig('buttonAction')

		try:
			method = getattr(self, action)
			method()
		except:
			self.logWarning(f'Button press detected but method **{action}** does not exist')


	def toggleMute(self):
		self.WakewordManager.toggleEngine()


	def startListening(self):
		if not self.getAliceConfig('deviceName') in self.DialogManager.sessionsBySites:
			self.DialogManager.onHotword(self.getAliceConfig('deviceName'))


	def stopSpeaking(self):
		self.AudioServer.stopPlaying()
