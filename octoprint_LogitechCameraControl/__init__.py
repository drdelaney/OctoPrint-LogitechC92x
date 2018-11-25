# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class LogitechCameraControlPlugin(octoprint.plugin.StartupPlugin,
					octoprint.plugin.SettingsPlugin,
					octoprint.plugin.TemplatePlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			v4l2ctlPath='/usr/bin/v4l2-ctl',
			focus_auto=True,
			focus_absolute=0,
			zoom_absolute=100,
			pan_absolute=0,
			tilt_absolute=0,
			brightness=128,
			contrast=128,
			saturation=128,
			gain=128,
			sharpness=128,
			backlight_compensation=0,
			white_balance_temperature_auto=True,
			white_balance_temperature=2482,
			exposure_auto_priority=False,
			exposure_auto=0,
			exposure_absolute=1000,
			power_line_frequency=2
		)

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	def on_after_startup(self):
		#self._logger.info("focus_auto",self._settings.get(['focus_auto']))
		self._logger.info("foo bar")
		# I dont know python iterated loops yet
	#	for mySetting,mySettingValue in self._settings():
	#		self._logger.info("{} = {}".format(mySetting,mySettingValue))

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			LogitechCameraControl=dict(
				displayName=self._plugin_name,
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="drdelaney",
				repo="OctoPrint-LogitechCameraControl",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/drdelaney/OctoPrint-LogitechCameraControl/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Logitech Camera Control"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = LogitechCameraControlPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

