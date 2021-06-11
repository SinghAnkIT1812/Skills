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
    country_names = country_names.replace(" ", ",")
    country_names= country_names.split(",")
    for x in country_names:
        cases.append(covid.get_status_by_country_name(x))
        root.update()
    for y in cases:
        confirmed.append(y["active"])
        deaths.append(y["deaths"])
        recoverd.append(y["recovered"])
    confirmed_patch=mpatches.Patch(colour='green',label='confirmed')
    recovered_patch=mpatches.Patch(colour='red',label='recovered')
    active_patch=mpatches.Patch(color='blue',label='active')
    deaths_patch=mpatches.Patch(color='black',label='deaths')
    plt.legend(handles=[confirmed_patch,recovered_patch,active_patch,deaths_patch)
    
                        
    for x in range(len(country_names)):
                        
                        plt.bar(country_names[x],confirmed[x],color='green')
                        
                        if recovered[x] > active[x]:
                             plt.
                        
                    
                        
