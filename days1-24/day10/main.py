# https://www.youtube.com/watch?v=KAmZe5D3v5I

import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

# HEALTH STATUS
g = (0.78, 0.78, 0.78)  # not infected
r = (0.96, 0.15, 0.15)  # infected
g = (0, 0.86, 0.03)  # recovered
b = (0, 0, 0)  # unalive

# COVID-19 PARAMETERS
# this can be re-used for other viruses/diseases

covid_params = {
    "r0": 2.28,  # measures how contagious a disease is
    "incubation": 5,  # days?
    "percent_mild": 0.8,  # percentage of cases that are mild?
    "mild_recovery": (7, 14),  # range of days to recover?
    "percent_severe": 0.2,  # percentage of cases that are severe?
    "severe_recovery": (21, 42),  # range of days to recover?
    "severe_death": (14, 56),  # range of days to unalive?
    "fatality_rate": 0.034,  # percentage of cases that unalive?
    # average time between excessive/successive?) cases in a chain transmission
    "serial_interval": 7
}


class Virus():
    def __init__(self, params):
        # Polar Plot
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111, projection="polar")
        self.axes.grid(False)
        self.axes.set_xticklabels([])  # x axis
        self.axes.set_yticklabels([])  # y axis
        self.axes.set_ylim(0, 1)  # y limit ?

        # Annotations
        # Day 0
        self.day_txt = self.axes.annotate(
            "Day 0", xy=[np.pi / 2, 1], ha="center", va="bottom"
            # x = pie / 2, y = 1
        )
        # Infected
        self.infected_txt = self.axes.annotate(
            "Infected: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=r
        )
        # Recoverd
        self.recovered_txt = self.axes.annotate(
            "\nRecovered: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=g
        )
        # Unalive
        self.unalive_txt = self.axes.annotate(
            "\nUnalive: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=b
        )

        # Variables
        self.day = 0  # days
        self.total_num_infected = 0  # total # infected
        self.num_currently_infected = 0  # currently infected
        self.num_recovered = 0  # total recovered
        self.num_deaths = 0  # total deaths

        self.r0 = params["r0"]
        self.percent_mild = params["percent_mild"]
        self.percent_severe = params["percent_severe"]
        self.fatality_rate = params["fatality_rate"]
        self.serial_interval = params["serial_interval"]

        # Mild infection
        # faster recovery
        self.mild_fast = params["incubation"] + params["mild_recovery"][0]
        # slower recovery
        self.mild_slow = params["incubation"] + params["mild_recovery"][1]

        # Severe infection
        self.severe_fast = params["incubation"] + params["severe_recovery"][0]
        self.severe_slow = params["incubation"] + params["severe_recovery"][1]

        # Unalive
        self.death_fast = params["incubation"] + params["death_recovery"][0]
        self.death_slow = params["incubation"] + params["death_recovery"][1]

        # Time Range (5yrs)
        self.mild = {i: {"thetas": [], "rs": []}
                     for i in range(self.mild_fast, 1825)}
