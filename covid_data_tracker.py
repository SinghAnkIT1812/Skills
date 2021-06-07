from tkinter import *
root = Tk()
root.geometry("350x350")
root.title("Get Covid-19 Data Country wise")


def showdata():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import covid
    covid = covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []


try:
    root.update()
    countries = data.get()
    country_names = countries.strip()
    country_names =
