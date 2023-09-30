from kt.log.logzero_demo import DB_LOG
from peewee import PostgresqlDatabase
from peewee import AutoField, DateTimeField, SQL
from peewee import Model as PeeweeModel

db = PostgresqlDatabase('postgres', user='postgres', password='950417', host='localhost')
# 初始化数据库连接
DB_LOG.info('正在连接数据库')
try:
    db.connect()
    DB_LOG.info('数据库连接成功')
except ConnectionError as e:
    DB_LOG.error(f'数据库连接失败:{e}')
    raise e


class _BaseModel(PeeweeModel):
    class Meta:
        database = db


class _BaseRecordModel(_BaseModel):
    id_ = AutoField(column_name='id', primary_key=True)
    created_at = DateTimeField(constraints=[SQL('DEFAULT NOW()')])
    updated_at = DateTimeField(constraints=[SQL('DEFAULT NOW()')])

    # def save(self, only=None, updated_at=None, force_insert=False,
    #          *args, **kwargs):
    #     if not force_insert:
    #         self.updated_at = updated_at or datetime.now(tzlocal())
    #     if only:
    #         only.append(self.__class__.updated_at)
    #     return super().save(only=only, force_insert=force_insert,
    #                         *args, **kwargs)
