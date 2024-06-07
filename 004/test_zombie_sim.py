from zombie_outbreak_sim import City, simulate_zombie_outbreak


def test_simulation():
    """
    Test that the simulate_zombie_outbreak function behaves as expected.
    """

    initial_grid = [
        ["H", "H", "H", "Z"],
        ["H", "H", "E", "H"],
        ["H", "H", "H", "H"],
        ["H", "H", "H", "H"],
    ]

    expected_grid_after_1_day = [
        ["H", "H", "Z", "Z"],
        ["H", "H", "E", "Z"],
        ["H", "H", "H", "H"],
        ["H", "H", "H", "H"],
    ]

    expected_grid_after_3_days = [
        ["Z", "Z", "Z", "Z"],
        ["H", "Z", "E", "Z"],
        ["H", "H", "Z", "Z"],
        ["H", "H", "H", "Z"],
    ]

    city = City(initial_grid)

    result_after_1_day = simulate_zombie_outbreak(city, 1)
    assert result_after_1_day == expected_grid_after_1_day, "Test case for 1 day failed"

    city = City(initial_grid)
    result_after_3_days = simulate_zombie_outbreak(city, 3)
    assert (
        result_after_3_days == expected_grid_after_3_days
    ), "Test case for 3 days failed"


if __name__ == "__main__":
    import pytest

    pytest.main(["-v", __file__])
