from pprint import pprint

from faker import Faker
from faker.providers import internet
from faker.providers import BaseProvider
from faker.providers import DynamicProvider

fake = Faker(['zh-CN'], use_weighting=False)

name = fake.name()
# pprint(name)
address = fake.address()
# pprint(address)


# fake.add_provider(internet)
# print(fake.ipv4_private())
# -----------------------------------
# 自定义字段
class MyField(BaseProvider):
    def test_field(self) -> str:
        return 'test_field'

fake.add_provider(MyField)
# pprint(fake.test_field())
# ------------------------------------
# 自定义动态字段
medical_professions_provider = DynamicProvider(
    provider_name="medical_profession",
    elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
)
fake.add_provider(medical_professions_provider)
# pprint(fake.medical_profession())  # 随机生成一个元素["dr.", "doctor", "nurse", "surgeon", "clerk"]
# --------------------------------------
# 自定义多个元素随机组合
my_word_list = ['danish ', 'cheesecake ', 'sugar ',
                'Lollipop ', 'wafer ', 'Gummies ',
                'sesame ', 'Jelly ', 'beans ',
                'pie ', 'bar ', 'Ice ', 'oat ']

fake.sentence()
# pprint(fake.sentence(ext_word_list=my_word_list))  # 随机组合几个元素 'Jelly oat Lollipop sesame Jelly Gummies .'
# ----------------------------------
"""
如果想生成相同的数据，搜索文档中：Seeding the Generator
"""