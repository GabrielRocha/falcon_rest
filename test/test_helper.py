from models import Amigo
import unittest
import helper

class TestHelper(unittest.TestCase):

    def setUp(self):
        self.amigo = Amigo(id=1,
                           nome='voce',
                           latitude=1,
                           longitude=2)
        self.amigo_2 = Amigo(id=2,
                             nome='2',
                             latitude=1,
                             longitude=3)
        self.amigo_3 = Amigo(id=3,
                             nome='3',
                             latitude=1,
                             longitude=4)
        self.amigo_4 = Amigo(id=4,
                             nome='4',
                             latitude=3,
                             longitude=1)
        self.amigo_5 = Amigo(id=5,
                             nome='5',
                             latitude=2,
                             longitude=2)

    def test_orm_to_json(self):
        json = helper.orm_to_json(self.amigo)
        self.assertEqual(json, {"nome": "voce",
                                "id": 1,
                                "latitude": 1,
                                "longitude": 2})

    def test_get_three_closer_friends(self):
        amigos_proximos = helper.get_three_closer_friends(self.amigo, [self.amigo_2,
                                                                       self.amigo_3,
                                                                       self.amigo_4,
                                                                       self.amigo_5
                                                                       ])
        self.assertEquals(len(amigos_proximos),3)
        self.assertIn((2,1.0), amigos_proximos)
        self.assertIn((3,2.0), amigos_proximos)
        self.assertIn((5,1.0), amigos_proximos)


    def test_get_hypotenuse(self):
        hipotenusa = helper.get_hypotenuse(self.amigo, self.amigo_2)
        self.assertEquals(round(hipotenusa,5), 1.0)

if __name__ == "__main__":
    unittest.main()
