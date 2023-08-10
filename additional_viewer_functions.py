from seticore import viewer as seticore_viewer
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

def plot_incoherent_beam(self):
    incoherent = np.square(self.real_array()).sum(axis=(2, 3, 4))
    snr, sig = self.snr_and_signal(incoherent)
    
    frequency = np.array(self.frequencies())
    time = np.array(self.times())
    time_diff = [x-time[0] for x in time]
    
    print(f"recalculated power: {sig:e}")
    print("local SNR:", snr)
    
    fig, ax = plt.subplots(figsize=(10, 2))
    
    xticks = np.array([float(x) for x in [0, 0/len(frequency), 20/len(frequency), 40/len(frequency), 60/len(frequency), 80/len(frequency), 100/len(frequency), 120/len(frequency)]])
    ax.set_xticklabels([f"{(frequency[0]*1000+tick*(frequency[-1]-frequency[0])*1000)-frequency[0]*1000:0.1f}" for tick in xticks], fontsize = 12)
    ax.set_xlabel(f"Frequency (kHz + {self.stamp.fch1:0.6f} MHz)", fontsize = 14)

    yticks = np.array([float(x) for x in [0, 0/len(time), 20/len(time), 40/len(time), 60/len(time)]])
    ax.set_yticklabels([f"{time_diff[0]+tick*(time_diff[-1]):0.3f}" for tick in yticks], fontsize = 12)
    ax.set_ylabel("Time (seconds)", fontsize = 14)
    
    ax.imshow(incoherent, rasterized=True, interpolation="nearest", cmap='viridis', aspect="auto")

def show_coherent_beam(self, beam):
    power = self.beamform_power(beam)
    snr, sig = self.snr_and_signal(power)
    
    print(f"recalculated power: {sig:e}")
    print("local SNR:", snr)
    
    frequency = np.array(stamps[7].frequencies())
    time = np.array(stamps[7].times())
    time_diff = [x-time[0] for x in time]
    
    fig, ax = plt.subplots(figsize=(10, 2))
    
    xticks = np.array([float(x) for x in [0, 0/len(frequency), 20/len(frequency), 40/len(frequency), 60/len(frequency), 80/len(frequency), 100/len(frequency), 120/len(frequency)]])
    ax.set_xticklabels([f"{(frequency[0]*1000+tick*(frequency[-1]-frequency[0])*1000)-frequency[0]*1000:0.1f}" for tick in xticks], fontsize = 12)
    ax.set_xlabel(f"Frequency (kHz + {self.stamp.fch1:0.6f} MHz)", fontsize = 14)

    yticks = np.array([float(x) for x in [0, 0/len(time), 20/len(time), 40/len(time), 60/len(time)]])
    ax.set_yticklabels([f"{time_diff[0]+tick*(time_diff[-1]):0.3f}" for tick in yticks], fontsize = 12)
    ax.set_ylabel("Time (seconds)", fontsize = 14)
    
    ax.imshow(power, rasterized=True, interpolation="nearest", cmap='viridis', aspect="auto")

def show_all_beam(a):
    
    power_0 = stamps[a].beamform_power(0)
    power_1 = stamps[a].beamform_power(1)
    power_2 = stamps[a].beamform_power(2)
    power_3 = stamps[a].beamform_power(3)
    power_4 = stamps[a].beamform_power(4)
    
    incoherent = np.square(stamps[a].real_array()).sum(axis=(2, 3, 4))
    
    frequency = np.array(stamps[a].frequencies())
    time = np.array(stamps[a].times())
    time_diff = [x-time[0] for x in time]
    
    fig = plt.figure(figsize = [15, 15])

    gs0 = gridspec.GridSpec(6, 8, figure=fig)

    ax1 = fig.add_subplot(gs0[0:1, 0:3])
    ax1.imshow(incoherent, rasterized=True, interpolation="nearest", cmap='viridis', aspect="auto")
    xticks = np.array([float(x) for x in [0, 0/len(frequency), 20/len(frequency), 40/len(frequency), 60/len(frequency), 80/len(frequency), 100/len(frequency), 120/len(frequency)]])
    ax1.set_xticklabels([f"{(frequency[0]*1000+tick*(frequency[-1]-frequency[0])*1000)-frequency[0]*1000:0.1f}" for tick in xticks], fontsize = 12)

    yticks = np.array([float(x) for x in [0, 0/len(time), 20/len(time), 40/len(time), 60/len(time)]])
    ax1.set_yticklabels([f"{time_diff[0]+tick*(time_diff[-1]):0.3f}" for tick in yticks], fontsize = 12)
    plt.tick_params('both', labelbottom = False, labelsize = 12)
    plt.ylabel("Incoherent Beam", fontsize = 11)

    # share x only
    ax2 = fig.add_subplot(gs0[1:2, 0:3], sharex=ax1, sharey=ax1)
    ax2.imshow(power_0, rasterized=True, interpolation="nearest", cmap='viridis', aspect="auto")
    # make these tick labels invisible
    plt.tick_params('both', labelbottom=False, labelsize = 12)
    plt.ylabel("Coherent Beam 1", fontsize = 11)

    # share x and y
    ax3 = fig.add_subplot(gs0[2:3, 0:3], sharex=ax1, sharey=ax1)
    ax3.imshow(power_1, rasterized=True, interpolation="nearest", cmap='viridis', aspect="auto")
    plt.tick_params('both', labelbottom=False, labelsize = 12)
    plt.ylabel("Coherent Beam 2", fontsize = 11)

    # share x and y
    ax4 = fig.add_subplot(gs0[3:4, 0:3], sharex=ax1, sharey=ax1)
    ax4.imshow(power_2, rasterized=True, interpolation="nearest", cmap='viridis', aspect="auto")
    plt.tick_params('both', labelbottom=False, labelsize = 12)
    plt.ylabel("Coherent Beam 3", fontsize = 11)

    # share x and y
    ax5 = fig.add_subplot(gs0[4:5, 0:3], sharex=ax1, sharey=ax1)
    ax5.imshow(power_3, rasterized=True, interpolation="nearest", cmap='viridis', aspect="auto")
    plt.tick_params('both', labelbottom=False, labelsize = 12)
    plt.ylabel("Coherent Beam 4", fontsize = 11)

    # share x and y
    ax6 = fig.add_subplot(gs0[5:6, 0:3], sharex=ax1, sharey=ax1)
    ax6.imshow(power_4, rasterized=True, interpolation="nearest", cmap='viridis', aspect="auto")
    plt.tick_params('both', labelsize = 12)
    plt.ylabel("Coherent Beam 5", fontsize = 11)
    plt.xlabel(f"Frequency (kHz + {stamps[a].stamp.fch1:0.6f} MHz)", fontsize = 14)
    
    plt.text(-35, -130, "Time (seconds)", fontsize = 14, rotation = 'vertical')

    ax7 = fig.add_subplot(gs0[1:-2, 4:])
    plt.scatter(recipes[6].ras[0], recipes[6].decs[0], label = 'Beam 1')
    plt.scatter(recipes[6].ras[1], recipes[6].decs[1], label = 'Beam 2')
    plt.scatter(recipes[6].ras[2], recipes[6].decs[2], label = 'Beam 3')
    plt.scatter(recipes[6].ras[3], recipes[6].decs[3], label = 'Beam 4')
    plt.scatter(recipes[6].ras[4], recipes[6].decs[4], label = 'Beam 5')
    
    plt.xlabel('Right Ascension', fontsize = 14)
    plt.ylabel('Declination', fontsize = 14)
    plt.grid()
    plt.legend()