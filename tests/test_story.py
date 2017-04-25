from py101 import Story


class TestStory(object):

    def test_name(self):
        assert Story().name == 'py101'
