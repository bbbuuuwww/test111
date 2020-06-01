from django.db import models

# Create your models here.

class Item(models.Model):
    #管道类
    url = models.URLField(unique=True, max_length=254)
    type = models.IntegerField()
    name = models.CharField(max_length=32)
    create_time = models.DateTimeField(db_index=True)
    update_time = models.DateTimeField(auto_now=True)
    def get_dict(self):
        return {"url":self.url,
                "type":self.type,
                "name":self.name,
                "create_time":self.create_time,
                "update_time":self.update_time
                }
    class Meta: # 元选类
        # db_table = “Item” # 生成数据库后的数据库名字
        unique_together = ["url", "type"] # 联合唯一索引
        index_together = ["type", "update_time"] # 联合索引

class Spider(models.Model):
    # 爬虫类
    source = models.URLField(max_length=254, unique=True, blank=False)
    spider_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    create_time = models.DateTimeField(db_index=True)
    update_time = models.DateTimeField(auto_now=True)

