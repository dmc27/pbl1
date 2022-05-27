
#-------------------------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
#-------------------------------------------------------------------

def imshow(img, cmap="gray", vmin=0, vmax=255, frameon=False, zoom=1.0):

  dpi = float(matplotlib.rcParams['figure.dpi'])/zoom

  fig = plt.figure(figsize=[img.shape[1]/dpi, img.shape[0]/dpi],
                   frameon=frameon)
  ax = fig.add_axes([0, 0, 1, 1])
  ax.axis('off')
  ax.imshow(img, cmap=cmap, vmin=vmin, vmax=vmax, interpolation='none')

  plt.show()
#-------------------------------------------------------------------

def imshow_horz(img1, img2, cmap="gray", vmin=0, vmax=255, frameon=False, zoom=1.0):

  dpi = float(matplotlib.rcParams['figure.dpi'])/zoom

  fig, (ax1, ax2) = plt.subplots(1, 2, 
    figsize=[2.5*img1.shape[1]/dpi, 10*img1.shape[0]/dpi], frameon=frameon)
  # ax = fig.add_axes([0, 0, 1, 1])
  ax1.axis('off')
  ax1.imshow(img1, cmap=cmap, vmin=vmin, vmax=vmax)
  ax2.axis('off')
  ax2.imshow(img2, cmap=cmap, vmin=vmin, vmax=vmax)

  plt.show()
#-------------------------------------------------------------------
