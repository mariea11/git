from nose.tools import *
from bin.Maps import *
from bin.StartGame import Engine

def test_room():
        coliseum = Room("Introduction",
                                        """This is the main room, here you choose to
                                        say Kitchen or Livngroom.""")
        assert_equal(Introduction.name, "Introduction")
        asser_equal(Introduction.paths, {})
        
def test_room_paths():
        yes = Room("Kitchen", "Move on.")
        no = Room("Livingroom", "Move on.")