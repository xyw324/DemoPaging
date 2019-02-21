import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DemoPaging.settings")

    import django
    django.setup()

    from app01 import models

    # for i in range(500):
        # 效率低的写法
        # models.Book.objects.create(title="跟老男孩学xx{}".format(i), price=i)

    # 高效的写法
    # 1. 先创建500个书籍对象
    book_list = [models.Book(title="海子的诗{}".format(i), price=i) for i in range(500)]
    # # 2. 批量提交到数据库,
    models.Book.objects.bulk_create(book_list)


