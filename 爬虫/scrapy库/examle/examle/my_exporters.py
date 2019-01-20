from scrapy.exporters import BaseItemExporter
import xlwt

class ExcelItemExporter(BaseItemExporter):
    def __init__(self,file,**kwargs):
        self._configure(kwargs)
        self.file = file
        # 创建Workbook和Worksheet对象，并初始化记录写入行坐标的self.row
        self.wbook = xlwt.Workbook()
        self.wsheet = self.wbook.add_sheet('scrapy')
        self.row = 0
    # 在所有数据都被写入Excel表格后调用save方法将Excel表格写入文件
    def finish_exporting(self):
        self.wbook.save(self.file)

    def export_item(self, item):
        # 调用基类的_get_ser..方法，获得item所有字段的迭代器，然后调用self.wsheet.write方法将各字段写入Excel表格
        fields = self._get_serialized_fields(item)
        for col,v in enumerate(x for _,x in fields):
            self.wsheet.write(self.row,col,v)
        self.row += 1