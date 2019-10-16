'''
@author: b33rnc0d3
@date: 2019-10-09
@version: 0.0.1

@TODO: 
    1. Add heatmap plot
    2. Add eCDF plot (empirical cumulative distribution function)
    3. Add KDE plot (kernel density estimate)
    4. Add pivot method for time series
    5. Add profile plot for pivot time series data

'''

import random
import numpy as np

from bokeh.plotting import figure
from bokeh.io import show, output_file, output_notebook
from bokeh.models import LinearAxis, Range1d

from bokeh.palettes import Category20 as palette

from random import randrange


class BokehEDAPlots:

    def __init__(
                    self, 
                    plot_width = 1700, 
                    plot_height = 800,
                    output_filename = "data.html"
                    ):
        '''
        '''

        self.__plot_width = plot_width
        self.__plot_height = plot_height
        self.__output_filename = output_filename

    def output_HTML(self):
        '''
            Writes plot data to HTML file
        
        '''
        output_file(self.__output_filename)

    def plot_scatter(
                        self,
                        x,
                        y, 
                        x_label = "",
                        y_label = "",
                        title = "",
                        color = "red",
                        alpha = 0.9
                        ):
        '''
        Example usage:

            plot_scatter(
                x = list(ahu3_wd.dewPoint),
                y = list(ahu3_wd.AHU_3_Supply_Dewpoint),
                x_label = "OA-Tdp",
                y_label = "DA-Tdp",
                title = "DA-Tdp vs. OA-Tdp",
                color = "red",
                alpha = 0.9
                )
        '''
        
        fig = figure(
                        plot_width = self.__plot_width,
                        plot_height = self.__plot_height,
                        title = title
                        )

        fig.scatter(x, y, color = color, alpha = alpha)

        fig.xaxis.axis_label = x_label

        fig.yaxis.axis_label = y_label

        fig.legend.location = "top_left"

        fig.legend.click_policy="hide"

        show(fig)


    def plot_datetime_line_1yaxis(
                                    self,
                                    x, 
                                    y : dict,  # { legend_title : data_series }
                                    x_label = "",
                                    y_label = "",
                                    title = "",
                                    alpha = 1.0,
                                    ):
        '''
        '''

        fig = figure(
                        plot_width = self.__plot_width,
                        plot_height = self.__plot_height,
                        x_axis_type = "datetime", 
                        title = title
                        )
    
        for key in y:

            k = random.choice( list(palette.keys()) )

            # choose random color from Category20 palette
            color = random.choice(palette[k])

            fig.line(
                        x, 
                        y[key], 
                        alpha = alpha, 
                        line_width = 1, 
                        color = color, 
                        legend = key
                        )
            
        fig.xaxis.axis_label = x_label
        fig.yaxis.axis_label = y_label
        
        fig.legend.location = "top_center"

        fig.legend.click_policy="hide"

        show(fig)


    def plot_datetime_line_2yaxis(
                                    self,
                                    x, 
                                    y1_dict : dict,        # { legend_title : data_series }
                                    y2_dict : dict,        # { legend_title : data_series }
                                    x_label = "",
                                    y1_label = "",
                                    y1_range = (0,100),    # tuple for y1 axis range
                                    y2_label = "" ,
                                    y2_range = (0,100),    # tuple
                                    title = "",
                                    alpha = 1.0
                                    ):
    
        fig = figure(
                        plot_width = self.__plot_width,
                        plot_height = self.__plot_height,
                        y_range = y1_range,
                        x_axis_type = "datetime",
                        title = title
                        )
        
        # unpack tuple of start / end range values
        start, end = y2_range

        fig.extra_y_ranges = {y2_label : Range1d(start = start ,end = end)}

        fig.add_layout(LinearAxis(y_range_name = y2_label, axis_label = y2_label), 'right')
        
        for key in y1_dict:
            # randomly generate colors for plot
            k = random.choice( list(palette.keys()) )
            color = random.choice(palette[k])
            
            fig.line(x, y1_dict[key], alpha = alpha, line_width = 1, color = color, legend = key)
            
        for key in y2_dict:
            # randomly generate colors for plot
            k = random.choice( list(palette.keys()) )
            color = random.choice(palette[k])
            
            fig.triangle(x, y2_dict[key], alpha = alpha, line_width = 1, color = color, legend = key, y_range_name = y2_label)
            fig.line(x, y2_dict[key], alpha = alpha, line_width = 1, color = color, legend = key, y_range_name = y2_label)    
        
        fig.xaxis.axis_label = x_label

        fig.yaxis[0].axis_label = y1_label
        fig.yaxis[1].axis_label = y2_label

        fig.legend.location = "top_center"

        fig.legend.click_policy = "hide"

        show(fig) 

    
    def plot_hist(
                    self,
                    data, 
                    bins,
                    title = "",
                    color = "blue",
                    alpha = 1.0
                    ):
        '''
        '''
        # generate histogram data and edges of bins from numpy
        hist, edges = np.histogram(
                                    data, 
                                    density = True, 
                                    bins = bins
                                    )
        
        fig = figure(
                        title = title ,
                        tools = '',
                        background_fill_color = "#fafafa"
                        )
        
        fig.quad(
                top = hist, 
                bottom = 0,
                left = edges[:-1],
                right = edges[1:],
                fill_color = "navy",
                line_color = "white",
                alpha = alpha
                )

        show(fig)


