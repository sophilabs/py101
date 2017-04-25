from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _


class Adventure(BaseAdventure):

    title = _('Introduction')

    def test(self, file):
        pass
