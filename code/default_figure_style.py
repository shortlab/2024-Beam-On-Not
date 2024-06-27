import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager

plt.rcParams['font.size'] = 20
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['legend.title_fontsize'] = '12'
plt.rcParams['lines.markersize'] = 8
plt.rcParams['figure.figsize'] = 6, 6

# set a custom font
fontname = 'Century Gothic' 
fontfile = [f for f in font_manager.findSystemFonts(fontpaths='/Users/alexisdevitre/Library/Fonts') if fontname in f][0]
font_manager.fontManager.addfont(fontfile)
plt.rcParams['font.family'] = fontname

palette_energy = sns.color_palette("magma", n_colors=4) #CMRmap_r, magma
colors_energies = {
    '150': palette_energy[0], 
    '800': palette_energy[1], 
    '1200': palette_energy[2], 
    '2400': palette_energy[3]
}

palette_tapes = sns.color_palette("viridis", n_colors=7) #CMRmap_r, magma
colors_tapes = {
    'f20': palette_tapes[0],
    'f23': palette_tapes[1],
    'f29': palette_tapes[2],
    'f33': palette_tapes[3],
    'f34': palette_tapes[4],
    'f28': palette_tapes[5],
    'f37': palette_tapes[6]
}

# Axes labels
label_suppression = 'Suppression $\mathrm{1 - I_c^{On} / I_c^{Off}}$'
label_degradation = 'Degradation $\mathrm{1 - I_c^{Off} / I_c^{Unirradiated}}$'

# output and input directories
outputDirectory = '../figures/raw/'
master = '../data/data-master-linear.xlsx'