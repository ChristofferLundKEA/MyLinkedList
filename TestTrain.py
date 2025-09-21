import unittest
from Train import Train
from Wagon import Wagon


class TrainTest(unittest.TestCase):

    # ---------- Lokomotiv-regler ----------
    def test_small_train_valid_locomotive_front(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        t.wagons.append(Wagon("Passenger:Seat"))
        self.assertTrue(t.validate())

    def test_small_train_invalid_missing_front_locomotive(self):
        t = Train()
        t.wagons.append(Wagon("Passenger:Seat"))
        t.wagons.append(Wagon("Goods"))
        self.assertFalse(t.validate())

    def test_large_train_valid_locomotive_front_and_back(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        for _ in range(9):
            t.wagons.append(Wagon("Passenger:Seat"))
        t.wagons.append(Wagon("Locomotive"))
        self.assertTrue(t.validate())

    def test_large_train_invalid_missing_back_locomotive(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        for _ in range(10):
            t.wagons.append(Wagon("Passenger:Seat"))
        self.assertFalse(t.validate())

    # ---------- Passager vs Gods ----------
    def test_goods_only_is_valid(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        t.wagons.append(Wagon("Goods"))
        self.assertTrue(t.validate())

    def test_passenger_then_goods_is_valid(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        t.wagons.append(Wagon("Passenger:Seat"))
        t.wagons.append(Wagon("Goods"))
        self.assertTrue(t.validate())

    def test_goods_before_passenger_invalid(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        t.wagons.append(Wagon("Goods"))
        t.wagons.append(Wagon("Passenger:Seat"))
        self.assertFalse(t.validate())

    # ---------- Sengevogne ----------
    def test_sleep_cars_together_valid(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        t.wagons.append(Wagon("Passenger:Sleep"))
        t.wagons.append(Wagon("Passenger:Sleep"))
        t.wagons.append(Wagon("Passenger:Seat"))
        self.assertTrue(t.validate())

    def test_sleep_cars_separated_invalid(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        t.wagons.append(Wagon("Passenger:Sleep"))
        t.wagons.append(Wagon("Passenger:Seat"))
        t.wagons.append(Wagon("Passenger:Sleep"))
        self.assertFalse(t.validate())

    # ---------- Spisevogn ----------
    def test_dining_accessible_valid(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        t.wagons.append(Wagon("Passenger:Seat"))
        t.wagons.append(Wagon("Passenger:Dining"))
        t.wagons.append(Wagon("Passenger:Sleep"))
        self.assertTrue(t.validate())

    def test_dining_blocked_by_sleep_invalid(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        t.wagons.append(Wagon("Passenger:Seat"))
        t.wagons.append(Wagon("Passenger:Sleep"))
        t.wagons.append(Wagon("Passenger:Dining"))
        self.assertFalse(t.validate())

    # ---------- Edge cases ----------
    def test_empty_train_invalid(self):
        t = Train()
        self.assertFalse(t.validate())

    def test_single_locomotive_valid(self):
        t = Train()
        t.wagons.append(Wagon("Locomotive"))
        self.assertTrue(t.validate())

    def test_single_passenger_invalid(self):
        t = Train()
        t.wagons.append(Wagon("Passenger:Seat"))
        self.assertFalse(t.validate())

    def test_single_goods_invalid(self):
        t = Train()
        t.wagons.append(Wagon("Goods"))
        self.assertFalse(t.validate())


if __name__ == "__main__":
    unittest.main()
