import pygame
import numpy as np
from simulation import helperfunctions
from simulation.agent import Agent
from experiments.flocking import parameters as p

"""
Specific boid properties and helperfunctions 
"""


class Boid(Agent):
    """ """
    def __init__(
        self, pos, v, flock, index: int, image: str="experiments/flocking/images/normal-boid.png"
    ) -> None:
        super(Boid, self).__init__(
            pos,
            v,
            image,
            max_speed=p.MAX_SPEED,
            min_speed=p.MIN_SPEED,
            mass=p.MASS,
            width=p.WIDTH,
            height=p.HEIGHT,
            dT=p.dT,
            index=index
        )

        self.flock = flock

    def update_actions(self) -> None:
        """ """

        # avoid any obstacles in the environment
        for obstacle in self.flock.objects.obstacles:
            collide = pygame.sprite.collide_mask(self, obstacle)
            if bool(collide):
                self.avoid_obstacle()

        align_force, cohesion_force, separate_force = self.neighbor_forces()
        # align_force, cohesion_force, separate_force = (
        #     np.zeros(2),
        #     np.zeros(2),
        #     np.zeros(2),
        # )

        # combine the vectors in one
        steering_force = (
            align_force * p.ALIGNMENT_WEIGHT
            + cohesion_force * p.COHESION_WEIGHT
            + separate_force * p.SEPARATION_WEIGHT
        )

        # adjust the direction of the boid
        self.steering += helperfunctions.truncate(
            steering_force / self.mass, p.MAX_FORCE
        )

    def neighbor_forces(self):
        """ """
        # find all the neighbors of a boid based on its radius view
        neighbors = self.flock.find_neighbors(self, p.RADIUS_VIEW)
        # TODO: one of the two performance problems is here: how much time it takes to compute the
        #  align_force, cohesion_force and separate_force for each neighbor
        pre_align_force, pre_cohesion_force, separate_force = self.flock.find_neighbor_velocity_center_separation(self, neighbors)
        #
        # if there are neighbors, estimate the influence of their forces
        if neighbors:
            align_force = self.align(pre_align_force)
            cohesion_force = self.cohesion(pre_cohesion_force)
        #
        else:
            align_force, cohesion_force = (
            np.zeros(2),
            np.zeros(2),
        )
        return align_force, cohesion_force, separate_force

    def align(self, neighbor_force):
        """Function to align the agent in accordance to neighbor velocity

        :param neighbor_force: np.array(x,y)

        """
        return helperfunctions.normalize(neighbor_force - self.v)

    def cohesion(self, neighbor_center):
        """Function to move the agent towards the center of mass of its neighbors

        :param neighbor_rotation: np.array(x,y)
        :param neighbor_center: 

        """
        force = neighbor_center - self.pos
        return helperfunctions.normalize(force - self.v)
