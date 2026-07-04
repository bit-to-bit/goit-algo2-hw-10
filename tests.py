import unittest
from main1 import randomized_quick_sort, deterministic_quick_sort
from main2 import Teacher, create_schedule

class TestAlgorithms(unittest.TestCase):
    def test_randomized_quick_sort(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(randomized_quick_sort(arr), sorted(arr))
        self.assertEqual(randomized_quick_sort([]), [])
        self.assertEqual(randomized_quick_sort([42]), [42])

    def test_deterministic_quick_sort(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(deterministic_quick_sort(arr), sorted(arr))
        self.assertEqual(deterministic_quick_sort([]), [])
        self.assertEqual(deterministic_quick_sort([42]), [42])

    def test_create_schedule_success(self):
        subjects = {'Математика', 'Фізика'}
        t1 = Teacher("О", "І", 45, "a@b.c", {'Математика', 'Фізика'})
        t2 = Teacher("Д", "Б", 35, "d@b.c", {'Фізика', 'Інформатика'})
        schedule = create_schedule(subjects, [t1, t2])
        self.assertIsNotNone(schedule)
        self.assertEqual(len(schedule), 1)
        self.assertEqual(schedule[0].first_name, "О")

    def test_create_schedule_age_priority(self):
        subjects = {'Фізика'}
        t1 = Teacher("О", "І", 45, "a@b.c", {'Фізика'})
        t2 = Teacher("Д", "Б", 35, "d@b.c", {'Фізика'})
        schedule = create_schedule(subjects, [t1, t2])
        self.assertIsNotNone(schedule)
        self.assertEqual(len(schedule), 1)
        self.assertEqual(schedule[0].first_name, "Д")

    def test_create_schedule_fail(self):
        subjects = {'Хімія'}
        t1 = Teacher("О", "І", 45, "a@b.c", {'Математика'})
        schedule = create_schedule(subjects, [t1])
        self.assertIsNone(schedule)

if __name__ == '__main__':
    unittest.main()
