import json
import codecs

class XHPipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open('data.json', 'w', encoding='utf-8')
        # 该方法用于处理数据

    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # 写入文件
        self.file.write(line)
        # 返回item
        return item
        # 该方法在spider被开启时被调用。

    def open_spider(self, spider):
        pass
        # 该方法在spider被关闭时被调用。

    def close_spider(self, spider):
        pass

class HongniangPipeline(object):

    def __init__(self):
        self.filename = codecs.open('content.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        html = json.dumps(dict(item), ensure_ascii=False)
        self.filename.write(html + '\n')
        return item

    def spider_closed(self, spider):
        self.filename.close()