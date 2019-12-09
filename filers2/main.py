"""Filers2 App
=====================

The main module that provides the app that runs the GUI.
"""
import filers2

from functools import partial
from os.path import join, dirname
import time

from base_kivy_app.app import BaseKivyApp, run_app as run_cpl_app
from base_kivy_app.app import report_exception_in_app
import cpl_media

from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty

from filers2.recording import PlayersContainerWidget
import filers2.processing

from kivy.core.window import Window

__all__ = ('Filers2App', 'run_app')


class Filers2App(BaseKivyApp):
    """The app which runs the GUI.
    """

    __config_props__ = ('player_num_rows', 'player_num_cols')

    yesno_prompt = ObjectProperty(None, allownone=True)
    '''Stores a instance of :class:`YesNoPrompt` that is automatically created
    by this app class. That class is described in ``base_kivy_app/graphics.kv``.
    '''

    players_widget: PlayersContainerWidget = ObjectProperty(None)

    player_num_rows = NumericProperty(None, allownone=True)
    """The number of rows used by the grid displaying all the players.

    If empty, :attr:`player_num_cols` must be set to a number, and then the
    rows will be auto-computed from the number of players added.
    """

    player_num_cols = NumericProperty(1, allownone=True)
    """The number of columns used by the grid displaying all the players.

    If empty, :attr:`player_num_rows` must be set to a number, and then the
    columns will be auto-computed from the number of players added.
    """

    @classmethod
    def get_config_classes(cls):
        d = super(Filers2App, cls).get_config_classes()
        d['recording'] = PlayersContainerWidget
        return d

    def get_config_instances(self):
        d = super(Filers2App, self).get_config_instances()
        d['recording'] = self.players_widget
        return d

    def __init__(self, open_player_thread=True, **kwargs):
        super(Filers2App, self).__init__(**kwargs)

    def build(self):
        base = dirname(filers2.__file__)
        Builder.load_file(join(base, 'filers2_style.kv'))

        self.yesno_prompt = Factory.FlatYesNoPrompt()
        root = Factory.get('MainView')()

        self.load_app_settings_from_file()
        self.apply_app_settings()

        return super(Filers2App, self).build(root)

    def on_start(self):
        self.set_tittle()

    def set_tittle(self, *largs):
        """ Sets the title of the window.
        """
        Window.set_title('Filers2 v{}, CPL lab'.format(filers2.__version__))

    def check_close(self):
        return True

    def clean_up(self):
        super(Filers2App, self).clean_up()

        if self.players_widget is not None:
            self.dump_app_settings_to_file()
            self.players_widget.clean_up()


def run_app():
    """The function that starts the GUI and the entry point for
    the main script.
    """
    cpl_media.error_callback = report_exception_in_app
    return run_cpl_app(Filers2App)
