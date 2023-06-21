"""Simulation in which infected cells (red) infect normal cells (white) upon contact and eventually become immune cells (green) after the recovery period."""
"""By: Justin Li"""
"""Email: jql@ad.unc.edu"""

from exercises.ex09 import constants
from exercises.ex09.model import Model
from exercises.ex09.view_controller import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model: Model = Model(constants.CELL_COUNT, constants.CELL_SPEED, constants.CELL_INFECT, constants.CELL_IMMUNE)
    view_controller: ViewController = ViewController(model)
    view_controller.start_simulation()


if __name__ == "__main__":
    main()