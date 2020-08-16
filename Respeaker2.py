from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Respeaker2(AliceSkill):
	"""
	Author: Psychokiller1888
	Description: Let's you configure the gpio button available on the device
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
