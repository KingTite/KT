from peewee import (CharField, IntegerField, DateField, TextField, BigIntegerField, BooleanField)

from src.app.Model import db, _BaseRecordModel


class DouYinAnchors(_BaseRecordModel):
    """抖音主播表"""
    short_id = CharField()
    douyin_id = CharField()
    anchor_id = CharField()
    nickname = CharField()
    head_image = CharField()
    gender = IntegerField()
    birthday = DateField()
    city = CharField()
    province = CharField()
    signature = TextField()
    telephone = CharField()
    fans_count = IntegerField()
    following_count = IntegerField()
    record_count = IntegerField()
    live_id = CharField()
    ticket_count = BigIntegerField()
    has_commerce_goods = BooleanField()
    aweme_count = IntegerField()
    cover_img = CharField()
    total_favorited = IntegerField()

    class Meta:
        table_name = 'douyin_anchors'
