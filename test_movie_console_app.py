import unittest
import movie_console_app


class TestToCheckMovieConsoleApp(unittest.TestCase):
    def test_to_add_movie(self):
        result = movie_console_app.add_movie("Hunter me")
        self.assertEqual(result,"movie Hunter me added successfully")