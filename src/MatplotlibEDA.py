##
# eda.py is a simple script used to assist the data cleaning and exploratory data analysis of time series data
#
# @author b33rNc0d3 (b33rnc0d3@protonmail.com)
# @version 0.0.2
# @date 2019-04-10
# 
# @TODO: 1. Update and test all functions
#        2. Add additional functionality

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MatplotlibEDAPlots:

    def __init__(
                    self,
                    figure_fname = None
                ):
        
        if figure_fname != None:
            self.__figure_fname = figure_fname
        
    # ------------------------------------------------------------------------------------------------------------
    # Helper Functions
    def saveFig(
                self, 
                plt, 
                fig, 
                fname
                ):
        '''
        '''
        if fname != None:
            fig.savefig(fname)
            plt.close(fig)
            
        return
    
    def plotLabels( 
                    self,
                    xlabel,
                    ylabel,
                    title 
                    ):
        '''
        '''
        plt.xlabel( xlabel )
        plt.ylabel( ylabel )
        plt.title( title )

    # ----------------------------------------------------------------------------------------------------------
    # Plot Wrapper Functions

    def plotScatter(
                    self,
                    xSeries,
                    ySeries,
                    xlabel=None,
                    ylabel=None,
                    title=None,
                    xlim = 20,
                    ylim = 10,
                    fname = None
                ):

        fig = plt.figure( figsize=(xlim,ylim) )
        
        plt.scatter( xSeries, ySeries, marker='.' )
        plotLabels( xlabel, ylabel, title )
        
        saveFig(plt, fig, fname)

    def empiricalCDF( series ):
        '''
        '''
        n = series.size
        x = np.sort( series )
        y = np.arange(1, n + 1 ) / n
        return x,y

    def plotEmpiricalCDF( 
                            self,
                            xSeries,
                            ySeries,
                            xlabel=None,
                            ylabel=None,
                            title=None, 
                            xlim = 20,
                            ylim = 10,
                            fname = None
                        ):
        '''
        '''
        fig = plt.figure( figsize=( xlim, ylim) )
        
        plt.plot( xSeries, ySeries, marker='.', linestyle='none' )
        plotLabels( xlabel, ylabel, title )
        
        saveFig(plt, fig, fname)

    def __pivotTimeSeries(
                            self,
                            series
                        ):
        '''
        '''
        time = pd.DataFrame([t.time() for t in series.index], index=series.index, columns=['time'])
        date = pd.DataFrame([d.date() for d in series.index], index=series.index, columns=['date'])
        
        result_df = pd.concat( [series, date, time], axis=1)
        pivot_df = pd.pivot_table( result_df, values=series.name, index = 'date', columns = 'time')
        
        return pivot_df

    def plotPivotTimeSeries(
                                self, 
                                series,
                                xlabel=None,
                                ylabel=None,
                                title=None, 
                                color = 'b',
                                xlim = 20,
                                ylim = 10, 
                                fname = None
                        ):
        '''
        '''
        # pivot series data(profile plots)
        pivot_df = self.__pivotTimeSeries(series)
        # plot pivoted series - 
        pivot_df.T.plot(legend=False,figsize=(xlim,ylim), color=color, alpha=0.4)
        #pivot_df.T.plot(legend=False, color=color, alpha=0.4)
        plotLabels( xlabel, ylabel, title )

    def plotJointDist( 
                        self,
                        xSeries,
                        ySeries,
                        xlim = 20,
                        ylim = 10,
                        statFunc = None,
                        fname = None
                    ):
        '''
        plotJointDist - plots the joint distribution of two series' of data
        '''
        
        plot = sns.jointplot( xSeries, ySeries, kind='kde', height=10, space=1, stat_func = statFunc )