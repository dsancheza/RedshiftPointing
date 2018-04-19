from dreampy.redshift.netcdf import RedshiftNetCDFFile
from dreampy.redshift.plots import RedshiftPlotChart
from dreampy.redshift.utils.correlate_lines import CrossCorrelation
import numpy
from scipy.stats import nanmean
import os.path
from genericFileSearch import genericFileSearch

class RSRRunTsys():
    def run(self, argv, obsNum):

        filename = genericFileSearch ('RedshiftChassis2', obsNum)
        nc = RedshiftNetCDFFile(filename)
        nc.hdu.get_cal()    
        pl  = RedshiftPlotChart()
        pl.plot_tsys(nc)
        #tsys = nanmean(nc.hdu.cal.Tsys.flatten())
	tsys_data = nc.hdu.cal.Tsys.flatten()
	tsys_data = tsys_data[numpy.where(numpy.isfinite(tsys_data))]
	tsys = numpy.median (tsys_data)
        print 'Average Tsys = %6.2f K' % tsys
        pl.hlines(tsys,70,115)
        pl.annotate("Average Tsys =%6.2fK on  Chassis %d"%(tsys,2), [114,tsys-1], fontsize=13, fontweight='bold', stretch='250', horizontalalignment='right', verticalalignment='top')
	pl.set_ylim(0.0,3*tsys)
        pl.savefig('rsr_summary.png', bbox_inches='tight')
