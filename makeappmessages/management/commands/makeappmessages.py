import os
from django.conf import settings
from django.utils.module_loading import import_module
from django.core.management.commands.makemessages import Command as Command_makemessages
from django.core.management.base import CommandError


class Command(Command_makemessages):
	help = (
		"Creates local message files only for project custom apps."
		" Applies makemessages command to each app in project directory."
		" Supports any native makemessages arguments."
	)

	def add_arguments(self, parser):
		super().add_arguments(parser)
		parser.add_argument(
			'--app',
			nargs='*',
			dest='app',
			help='Applications to make message files for',
		)
	@staticmethod
	def get_local_app_list():
		"""
		List of all apps that are located inside project directory.
		This ensures that message files are made only for custom apps.
		"""
		app_list = [
			{
				'name': app,
				'dir': os.path.dirname(os.path.abspath(import_module(app).__file__)),
			}
			for app in settings.INSTALLED_APPS
		]
		return [app for app in app_list if settings.BASE_DIR in app['dir']]

	def handle(self, *args, **options):
		local_app_list = Command.get_local_app_list()
		if options.get('app'):
			print('app arg present')
			for app_name in options['app']:
				if app_name not in settings.INSTALLED_APPS:
					raise CommandError('Given application name \"%s\" is not in INSTALLED_APPS' % app_name)
			# filter local_app_list to contain only apps that are given to management command
			local_app_list = [app for app in local_app_list if app['name'] in options['app']]
			# remove app from options dict
			del options['app']


		for app in local_app_list:
			os.chdir(app['dir'])
			# explicitly create "locale" directory in each app directory and
			# execute super().handle() for each app, switching the app directory respectively
			locale_dir_path = os.path.join(app['dir'], 'locale')
			if not os.path.exists(locale_dir_path):
				os.makedirs(locale_dir_path)
			super().handle(*args, **options)
		# change dir back to origin
		os.chdir(settings.BASE_DIR)
