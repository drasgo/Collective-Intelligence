import numpy as np
from experiments.flocking.boid import Boid
from experiments.flocking import parameters as p
from simulation.swarm import Swarm
from simulation import helperfunctions

"""
Specific flock properties, and flocking environment definition 
"""


class Flock(Swarm):  # also access methods from the super class Swarm
    """ """
    def __init__(self, screen_size):
        super(Flock, self).__init__(screen_size)
        self.object_loc = p.OUTSIDE

    def initialize(self, num_agents: int):
        """

        :param num_agents:

        """

        # add obstacle/-s to the environment if present
        if p.OBSTACLES:
            object_loc = p.OBJECT_LOC

            if p.OUTSIDE:
                scale = [300, 300]
            else:
                scale = [800, 800]

            filename = (
                "experiments/flocking/images/convex.png"
                if p.CONVEX
                else "experiments/flocking/images/redd.png"
            )

            self.objects.add_object(
                file=filename, pos=object_loc, scale=scale, type="obstacle"
            )

            min_x, max_x = helperfunctions.area(object_loc[0], scale[0])
            min_y, max_y = helperfunctions.area(object_loc[1], scale[1])

        # add agents to the environment
        for index, agent in enumerate(range(num_agents)):
            coordinates = helperfunctions.generate_coordinates(self.screen)

            # if obstacles present re-estimate the corrdinates
            if p.OBSTACLES:
                if p.OUTSIDE:
                    while (
                            max_x >= coordinates[0] >= min_x
                            and max_y >= coordinates[1] >= min_y
                    ):
                        coordinates = helperfunctions.generate_coordinates(self.screen)
                else:
                    while (
                        coordinates[0] >= max_x
                        or coordinates[0] <= min_x
                        or coordinates[1] >= max_y
                        or coordinates[1] <= min_y
                    ):
                        coordinates = helperfunctions.generate_coordinates(self.screen)

            self.add_agent(Boid(pos=np.array(coordinates), v=None, flock=self, index=index))

    # def find_neighbor_velocity(self, neighbors):
    #     """
    #
    #     :param neighbors:
    #
    #     """
    #     neighbor_sum_v = np.zeros(2)
    #     for idx in neighbors:
    #         neighbor_sum_v += list(self.agents)[idx].v
    #     return neighbor_sum_v / len(neighbors)
    #
    # def find_neighbor_center(self, neighbors):
    #     """
    #
    #     :param neighbors:
    #
    #     """
    #     neighbor_sum_pos = np.zeros(2)
    #     for idx in neighbors:
    #         neighbor_sum_pos += list(self.agents)[idx].pos
    #     return neighbor_sum_pos / len(neighbors)
    #
    # def find_neighbor_separation(self, boid, neighbors):  # show what works better
    #     """
    #
    #     :param boid:
    #     :param neighbors:
    #
    #     """
    #     separate = np.zeros(2)
    #     for idx in neighbors:
    #         neighbor_pos = list(self.agents)[idx].pos
    #         difference = (
    #             boid.pos - neighbor_pos
    #         )  # compute the distance vector (v_x, v_y)
    #         difference /= helperfunctions.norm(
    #             difference
    #         )  # normalize to unit vector with respect to its maginiture
    #         separate += difference  # add the influences of all neighbors up
    #     return separate / len(neighbors)

    def find_neighbor_velocity_center_separation(self, boid, neighbors):
        neighbor_sum_v, neighbor_sum_pos, separate = (
            np.zeros(2),
            np.zeros(2),
            np.zeros(2),
        )

        for neigh in neighbors:
            # print(neighbors)
            # neigh = self.agents[idx]
            neighbor_sum_v += neigh.v
            neighbor_sum_pos += neigh.pos
            difference = (
                    boid.pos - neigh.pos
            )  # compute the distance vector (v_x, v_y)
            difference /= helperfunctions.norm(
                difference
            )  # normalize to unit vector with respect to its maginiture
            separate += difference  # add the influences of all neighbors up

        return neighbor_sum_v / len(neighbors), neighbor_sum_pos / len(neighbors), separate / len(neighbors)

