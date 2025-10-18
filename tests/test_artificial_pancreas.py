from main.artificial_pancreas import ArtificialPancreasSystem
import pytest

@pytest.fixture
def data():
    return ArtificialPancreasSystem(glucose_level=100, insulin_sensitivity=1.0, target_glucose=100, tolerance=10)

def test_glucose_increases_after_meal(system):
    #TODO
    pass

def test_glucose_never_below_min(system):
    # TODO
    pass

def test_glucose_decreases_after_excercise(system):
    # TODO
    pass
