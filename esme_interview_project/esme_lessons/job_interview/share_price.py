"""
Exercise 4: SHARE PRICE - Level Medium

Your goal is to write a function and it's unit test.
This function should do the following task:

Given a list representing the evolution of shares prices of a company over a period of time.
Let's say each point is one day.
I want to find at which days I should have bought a share and sell it in order to have the maximum margin.

Examples
    share = [2, 3.5, 4, 4.2, 4.1, 3.0, 5.0, 1.0, 1.2, 1.6]
    share_price(share)
    -> day to buy: 1, day to sell: 7, margin: 3

Try to find an optimal way of doing it if possible ;)

"""

import matplotlib.pyplot as plt


def display_share(share):
    """
    This function plot the share price over time.

    :param list share: evolution of shares prices of a company over a period of time
    :return: nothing
    """
    plt.plot(share)
    plt.show()


def share_price(share):
    """
    This function get the day where I should buy a share, the day I should sell it
    and the best margin I could have.

    :param list share: evolution of shares prices of a company over a period of time
    :return: The day where I should buy, The day where I should sell the share and the obtained margin.
    :rtype: int, int, int
    """
    # TODO
    # return day_to_buy, day_to_sell, margin
    pass
