# -*- coding: utf-8 -*- 
from ui.myframe import MyFrame1
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map


class MyFrame(MyFrame1):
    def __init__(self,parent):
        MyFrame1.__init__(self,parent)
        pass
    def load( self, event):
        #file=open(self.filename.GetValue(), encoding='gbk')
        file=pd.read_csv(self.filename.GetValue(), encoding='gbk',header=None)  
        if self.mapchoice.GetStringSelection()=="世界地图":
            maptype="world"
        elif  self.mapchoice.GetStringSelection()=="香港地图":    
            maptype="香港"
        elif self.mapchoice.GetStringSelection()=="中国地图":
            maptype="china"
        elif self.mapchoice.GetStringSelection()=="广东地图":
            maptype="广东"
        c = (
            Map()
            .add("", np.array(file).tolist(), maptype,is_map_symbol_show=False)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=self.m_checkBox1.GetValue()))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=self.mapname.GetValue()),
                visualmap_opts=opts.VisualMapOpts(max_=self.maxvalue.GetValue()))
            .render(self.save.GetValue())
        ) 