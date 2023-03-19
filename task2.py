# Define all functions for Task 2 here.

import numpy as np

def reconstruct_prices(orders, totals):
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
