'''Plots trips with a summary smoothing plot.'''

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
  
def add_inset(fig, ax, rect, *args, **kwargs):
  box = ax.get_position()
  inax_position = ax.transAxes.transform(rect[0:2])
  infig_position = ax.figure.transFigure.inverted().transform(inax_position)
  new_rect = list(infig_position) + [box.width * rect[2], box.height * rect[3]]
  return fig.add_axes(new_rect, *args, **kwargs)

# Plots the trip data
# Input: trips - trips data
def plotTrips(trips, columns=['Annual Member', 'Short-Term Pass Holder']):
  # Restructure the data
# Find the start date
  by_date = trips.pivot_table('trip_id', 
                              aggfunc='count',
                              index='date',
                              columns='usertype', 
                             )
  weekly = by_date.pivot_table(columns,
                               index=by_date.index.weekofyear,
                               columns=by_date.index.dayofweek,
                              )
  # Create the plot structure
  fig, ax = plt.subplots(2, 1, figsize=(16, 8), sharex=True, sharey=True)
  fig.subplots_adjust(hspace=0.1)
  #
  color_cycle = plt.rcParams['axes.color_cycle']
  for i, col in enumerate(columns):
    by_date[col].plot(ax=ax[i], title=col, color=color_cycle[i])
    ax[i].set_title(col + 's')
  # 
  with sns.axes_style('whitegrid'):
    inset = [add_inset(fig, ax[0], [0.07, 0.6, 0.2, 0.32]),
             add_inset(fig, ax[1], [0.07, 0.6, 0.2, 0.32])]
  
  # Construct the plots
  for i, col in enumerate(['Annual Member', 'Short-Term Pass Holder']):
    inset[i].plot(range(7), weekly[col].values.T, color=color_cycle[i], lw=2, alpha=0.05);
    inset[i].plot(range(7), weekly[col].mean(0), color=color_cycle[i], lw=3)
    inset[i].set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    inset[i].yaxis.set_major_locator(plt.MaxNLocator(5))
    inset[i].set_ylim(0, 500)
    inset[i].set_title('Average by Day of Week')
      
  fig.savefig('figs/daily_trend.png', bbox_inches='tight')

if __name__ == "__main__":
  import path_utils
  import data_access as da
  trips = da.getTripsData()
  plotTrips(trips)
