from datetime import datetime
from pprint import pprint

import factory

from log.logzero_demo import FAKER_LOG
from src.app.Model.douyon_anchors import DouYinAnchors


class DouYinAnchorsFactory(factory.Factory):
    class Meta:
        model = DouYinAnchors

    # 模型字段与fake字段绑定
    id = factory.sequence(lambda n: n + 1)
    short_id = factory.Faker('name', locale='zh_CN')
    douyin_id = factory.Faker('name', locale='zh_CN')
    anchor_id = factory.Faker('name', locale='zh_CN')
    nickname = factory.Faker('name', locale='zh_CN')
    head_image = factory.Faker('name', locale='zh_CN')
    gender = factory.Faker('random_digit', locale='zh_CN')
    birthday = factory.Faker('date', locale='zh_CN')
    city = factory.Faker('city', locale='zh_CN')
    province = factory.Faker('city', locale='zh_CN')
    signature = factory.Faker('text', locale='zh_CN')
    telephone = factory.Faker('phone_number', locale='zh_CN')
    fans_count = factory.Faker('random_digit', locale='zh_CN')
    following_count = factory.Faker('random_digit', locale='zh_CN')
    record_count = factory.Faker('random_digit', locale='zh_CN')
    live_id = factory.Faker('name', locale='zh_CN')
    ticket_count = factory.Faker('random_digit', locale='zh_CN')
    has_commerce_goods = factory.Faker('boolean', locale='zh_CN')
    aweme_count = factory.Faker('random_digit', locale='zh_CN')
    cover_img = factory.Faker('name', locale='zh_CN')
    total_favorited = factory.Faker('random_digit', locale='zh_CN')
    created_at = factory.LazyFunction(datetime.now)
    updated_at = factory.LazyFunction(datetime.now)


if __name__ == '__main__':
    # 生成假数据
    anchors = DouYinAnchorsFactory.build_batch(100)

    # 去除唯一约束冲突
    anchor_ids = [row.anchor_id for row in DouYinAnchors.select(DouYinAnchors.anchor_id)]
    data_list = []
    for anchor in anchors:
        anchor_dict = anchor.__data__
        if anchor_dict['anchor_id'] in anchor_ids:
            continue
        else:
            anchor_ids.append(anchor_dict['anchor_id'])
        anchor_dict.pop('id')
        data_list.append(anchor_dict)
    # 批量插入
    try:
        DouYinAnchors.insert_many(data_list).execute()
        FAKER_LOG.info(f'成功为 DouYinAnchors 添加 {len(data_list)} 条假数据')
    except Exception as e:
        FAKER_LOG.error(f'添加数据失败：{e}')
        raise e
