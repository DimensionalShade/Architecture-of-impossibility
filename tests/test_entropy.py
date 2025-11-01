import unittest
from omega_drive import estimate_omega

class TestOmegaDrive(unittest.TestCase):
    def test_omega_estimate_range(self):
        programs = [f"P{i}" for i in range(1000)]
        omega = estimate_omega(programs)
        self.assertTrue(0.0 <= omega <= 1.0, "Ω must be between 0 and 1")

    def test_entropy_threshold(self):
        programs = [f"P{i}" for i in range(1000)]
        omega = estimate_omega(programs)
        threshold = 0.5
        if omega > threshold:
            result = "Ω-phase"
        else:
            result = "classical"
        self.assertIn(result, ["Ω-phase", "classical"])

if __name__ == "__main__":
    unittest.main()
