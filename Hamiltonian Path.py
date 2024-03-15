import itertools
import PySimpleGUI as Py
import numpy as np

# create all hamiltonian paths for a connected graph

Py.theme('DarkGreen2')  # theme
# All the stuff inside window.
layout = [[Py.Text('Enter the number of points'), Py.InputText()],
          [Py.Button('Hamilton path'), Py.Button('Cancel')]]

# Create the Window
window = Py.Window('Hamilton Paths', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == Py.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    m = list(range(1, (int(values[0]) + 1)))

    perm = list(itertools.permutations(m, len(m)))

    arr = np.matrix(perm)
    print(arr)

    comb = list(itertools.combinations(m, 2))
    print(comb)

    dict1 = {}
    r = 0
    for i in range(len(comb)):
        a = str(comb[r])
        dict1[a] = input("Enter the weight of" + a + "in integer format:")
        r = r + 1

    print(dict1)
