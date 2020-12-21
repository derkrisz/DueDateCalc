import unittest, due_date_calc

class TestDueDateCalculator(unittest.TestCase):

    def setUp(self):
        self.input = 'Thursday 4:15 PM'

    def test_get_am_pm(self):
        am_pm = due_date_calc.get_am_pm(self.input)
        self.assertEqual(am_pm, 'PM')

    def test_get_time(self):
        time = due_date_calc.get_time(self.input)
        output = ['4', '15']
        self.assertListEqual(time, output)
        
    def test_get_day(self):
        day = due_date_calc.get_day(self.input)
        self.assertEqual(day, 'THURSDAY')

    def test_am_pm_exception(self):
        input = 'Tuesday 2:14 fz'
        with self.assertRaises(ValueError) as e:
            result = due_date_calc.get_am_pm(input)
        self.assertEqual(str(e.exception),'Time of day should be AM or PM')

    def test_invalid_hours_exception(self):
        invalid_hour = 'Sunday 14:50 pm'
        with self.assertRaises(ValueError) as e:
            result = due_date_calc.get_time(invalid_hour)
        self.assertEqual(str(e.exception), 'Hours should be between 1 and 12')

    def test_invalid_minutes_exception(self):
        invalid_minutes = 'Thursday 12:60 am'
        with self.assertRaises(ValueError) as e:
            result = due_date_calc.get_time(invalid_minutes)
        self.assertEqual(str(e.exception), 'Minutes should be between 0 and 60')

    def test_day_exception(self):
        input = 'Monnday 3:13 am'
        with self.assertRaises(ValueError) as e:
            result = due_date_calc.get_day(input)
        self.assertEqual(str(e.exception),"Day should be a day of the week e.g. 'Monday', 'Tuesday'")





if __name__ == '__main__':
    unittest.main()