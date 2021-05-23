# import numpy
import pygame

# from simulation.agent import Agent
from simulation.helperfunctions import dist
from simulation.objects import Objects

"""
General swarm class that defines general swarm properties, which are common across different swarm types
"""

# superclass
class Swarm(pygame.sprite.Sprite):
    """ """
    def __init__(self, screen_size, plot=None) -> None:
        super(Swarm, self).__init__()
        self.dist_temp = {}
        self.agents = []
        self.screen = screen_size
        self.objects = Objects()
        self.points_to_plot = plot
        self.datapoints = []

    def add_agent(self, agent) -> None:
        """

        :param agent: 

        """
        self.agents.append(agent)

    def compute_distance(self, a, b) -> float:
        """

        :param a: 
        :param b: 

        """
        indexes = (a.index, b.index)
        pair = (min(indexes), max(indexes))

        if pair not in self.dist_temp:
            self.dist_temp[pair] = dist(a.pos, b.pos)
        return self.dist_temp[pair]

    def find_neighbors(self, agent, radius):
        """

        :param agent: param radius:
        :param radius: 

        """
        #  Slight improvement like that
        return [neighbor for neighbor in self.agents if
                agent is not neighbor and
                neighbor.type in [None, "I"] and
                self.compute_distance(agent, neighbor) < radius]
        # neighbors = []
        #
        # for neighbor in self.agents:
        #     if agent != neighbor and \
        #             (neighbor.type in [None, "I"]) and \
        #              self.compute_distance(agent, neighbor) < radius:  #TODO: one of the two performance problems is here: how much time it takes to compute the euclidean distance between the two "vectors"
        #            neighbors.append(neighbor)
        # return neighbors

    def remain_in_screen(self) -> None:
        """ """
        for agent in self.agents:
            if agent.pos[0] > self.screen[0]:
                agent.pos[0] = 0.0
            if agent.pos[0] < 0:
                agent.pos[0] = float(self.screen[0])
            if agent.pos[1] < 0:
                agent.pos[1] = float(self.screen[1])
            if agent.pos[1] > self.screen[1]:
                agent.pos[1] = 0.0

    # plotting the number of infected and recovered
    def add_point(self, lst) -> None:
        """

        :param lst: 

        """
        # Count current numbers
        values = {"S": 0, "I": 0, "R": 0}
        for state in lst:
            values[state] += 1

        for x in values:
            self.points_to_plot[x].append(values[x])

    def update(self) -> None:
        """ """
        # update the movement
        self.datapoints = []
        for agent in self.agents:
            agent.update_actions()

        if len(self.datapoints):
            self.add_point(self.datapoints)
        self.remain_in_screen()

    def display(self, screen: pygame.Surface) -> None:
        """

        :param screen: pygame.Surface:

        """
        for obstacle in self.objects.obstacles:
            obstacle.display(screen)

        for site in self.objects.sites:
            site.display(screen)

        for agent in self.agents:
            agent.update()
            agent.display(screen)
            agent.reset_frame()

        self.dist_temp = {}
