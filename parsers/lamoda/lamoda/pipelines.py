from itemadapter import ItemAdapter
from lamoda.database import DB, insert


class LamodaPipeline:
    def process_item(self, item, spider):
        itemdict = item.__dict__['_values']
        insert(DB(**itemdict))
        return item
