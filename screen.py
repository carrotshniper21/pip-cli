import npyscreen

import emulation
import util


class SelectGenreForm(npyscreen.Form):
    def create(self):
        self.genre_links = emulation.get_genres(self.parentApp.web_driver)
        emulation.display_genres_to_user(self.genre_links)
        self.genre_choice = self.add(npyscreen.TitleText, name="Genre choice:")
        self.next_button = self.add(npyscreen.ButtonPress, name="Next")

    def on_ok(self):
        if emulation.validate_user_genre_choice(self.genre_choice.value, self.genre_links):
            self.parentApp.getForm("SELECT_MOVIE").genre_links = self.genre_links
            self.parentApp.getForm("SELECT_MOVIE").user_choice = self.genre_choice.value
            self.parentApp.switchForm("SELECT_MOVIE")
        else:
            npyscreen.notify_wait("Invalid genre choice. Please try again.")

    def on_cancel(self):
        self.parentApp.switchForm(None)


class SelectMovieForm(npyscreen.Form):
    def create(self):
        self.genre_links = None
        self.user_choice = None
        self.movies = self.add(npyscreen.TitleMultiSelect, max_height=4, name="Movies:", values=movies)
        self.back_button = self.add(npyscreen.ButtonPress, name="Back")
        self.watch_button = self.add(npyscreen.ButtonPress, name="Watch")

    def beforeEditing(self):
        movie_src, self.titles = emulation.user_choice_validator_loop(self.user_choice, self.genre_links,
                                                                      self.parentApp.web_driver)
        self.movies.values = self.titles

    def on_ok(self):
        self.parentApp.selected_movie = self.movies.get_selected_objects()[0]
        self.parentApp.switchForm(None)

    def on_cancel(self):
        self.parentApp.switchForm("SELECT_GENRE")

    def on_watch(self):
        self.parentApp.selected_movie = self.movies.get_selected_objects()[0]
        self.parentApp.switchForm(None)


class MovieApp(npyscreen.NPSAppManaged):
    def onStart(self):
        if util.internet_working():
            browser_choice = input("Enter browser choice (1 for Firefox, 2 for Chrome): ")
            self.web_driver = emulation.validate_browser_choice(browser_choice)
            self.addForm("SELECT_GENRE", SelectGenreForm)
            self.addForm("SELECT_MOVIE", SelectMovieForm)
        else:
            npyscreen.notify_wait("No internet connection detected. Exiting...")
            self.switchForm(None)
