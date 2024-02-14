import unittest

from src.poisson_disk import PoissonDisk


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.poisson_disk = PoissonDisk(800, 600, 50, 30)
        self.poisson_disk.poisson_disk_sampling()

    def test_poisson_disk_sampling_dont_return_an_empty_list(self):
        self.assertTrue(self.poisson_disk.samples != [])

    def test_poisson_disk_sampling_distance_btw_2point(self):
        l = len(self.poisson_disk.samples)
        for i in range(l):
            for j in range(i + 1, l):
                distance = self.poisson_disk.samples[i].distance(self.poisson_disk.samples[j])
                self.assertTrue(distance >= self.poisson_disk.radius)


if __name__ == '__main__':
    unittest.main()
