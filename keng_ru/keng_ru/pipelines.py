from itemadapter import ItemAdapter
from keng_ru.database import DB, insert


class KengRuPipeline:
    def process_item(self, item, spider):
        itemdict = item.__dict__['_values']
        insert(DB(**itemdict))
        return item
