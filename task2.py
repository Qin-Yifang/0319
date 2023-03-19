# Define all functions for Task 2 here.

import numpy as np

def reconstruct_prices(orders, totals):
    """
    Reconstructs the prices of individual widgets given a list of orders and
    their corresponding totals.

    Args:
    - orders (list of lists of strings): A list of orders, where each order is a
      list of strings representing the widgets ordered.
    - totals (list of floats): A list of floats representing the total cost of
      each order.

    Returns:
    - A list of floats representing the price of each widget type, in the order
      they appear in the input orders.
    """
    widget_names = {}
    count = 0
    for order in orders:
        for widget in order:
            if widget not in widget_names:
                widget_names[widget] = f'w{count}'
                count += 1
    
    A = np.zeros((len(orders), len(widget_names)))
    for i, order in enumerate(orders):
        for widget in order:
            A[i, list(widget_names.keys()).index(widget)] += 1
    
    x, residuals, rank, s = np.linalg.lstsq(A, totals, rcond=None)
    
    prices = np.round(x, 2)
    
    return list(prices)


def price(widget, r, y, b):
    """
    Computes the price of a given widget or combination of widgets, based on the
    prices of the individual color components.

    Args:
    - widget (string or list of strings): A string representing a single widget
      color, or a list of strings representing a combination of widgets.
    - r (float): The price of a red widget.
    - y (float): The price of a yellow widget.
    - b (float): The price of a blue widget.

    Returns:
    - A float representing the price of the given widget or combination of widgets.
    """
    if isinstance(widget, str):
        if widget == 'RED':
            return r
        elif widget == 'YELLOW':
            return y
        elif widget == 'BLUE':
            return b
    else:
        total_price = 0
        for subwidget in widget:
            total_price += price(subwidget, r, y, b)
        return total_price

def constituents(widget):
    """
    Computes the number of red, yellow, and blue widgets that make up a given
    widget or combination of widgets.

    Args:
    - widget (string or list of strings): A string representing a single widget
      color, or a list of strings representing a combination of widgets.

    Returns:
    - A list of three integers representing the number of red, yellow, and blue
      widgets that make up the given widget or combination of widgets, in that order.
    """
    nr = 0
    ny = 0
    nb = 0
    if isinstance(widget, str):
        if widget == 'RED':
            nr += 1
        elif widget == 'YELLOW':
            ny += 1
        elif widget == 'BLUE':
            nb += 1
    else:
        for sub_widget in widget:
            nr_sub, ny_sub, nb_sub = constituents(sub_widget)
            nr += nr_sub
            ny += ny_sub
            nb += nb_sub
    return [nr, ny, nb]
