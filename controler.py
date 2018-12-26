#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from sekaoku_table import Post, User, Heritage, Base


class SekaokuController(object):
    def __init__(self):
        self.session = None

    def make_session(self):
        engine = create_engine('sqlite:///', echo=True)
        Base.metadata.create_all(engine)
        session_maker = sessionmaker(bind=engine)
        self.session = session_maker()
        return self.session

    def add_user(self, name):
        user = User(name=name)
        self.session.add(user)

    def add_heritage(self, name_en, name_jp, state_en, state_jp, longitude, latitude):
        heritage = Heritage(name_en=name_en, name_jp=name_jp,
                            state_en=state_en, state_jp=state_jp,
                            longitude=longitude, latitude=latitude
                            )
        self.session.add(heritage)

    def add_post(self, user_id, heritage_id, type, image_full_url, image_thumbnail_url, date):
        post = Post(user_id=user_id, heritage_id=heritage_id,
                    type=type,
                    image_full_url=image_full_url,
                    image_thumbnail_url=image_thumbnail_url,
                    date=date)
        self.session.add(post)

    def begin(self):
        return self.session.begin(subtransactions=True)

    def close(self):
        self.session.close()

    def is_new_user(self, name):
        # TODO impliment
        return True

    def find_heritage_id(self, name_en):
        # TODO impliment
        return 1

def main():
    sekaoku_ctr = SekaokuController()
    sekaoku_ctr.make_session()

    with sekaoku_ctr.begin():
        # add user
        for i in range(5):
            sekaoku_ctr.add_user(name="Alice")

        # add heritage
        for i in range(5):
            sekaoku_ctr.add_heritage(name_en='Mt Fuji',
                                     name_jp='富士山',
                                     state_en='japanese highest mountain',
                                     state_jp='日本一高い山',
                                     longitude=35.360556,
                                     latitude=138.727778
                                     )

        # add post
        for i in range(5):
            sekaoku_ctr.add_post(user_id=i+1, heritage_id=i+1,
                                 type="place",
                                 image_full_url="http://sample_image.com",
                                 image_thumbnail_url="http://sample_thumbnail_image.com",
                                 date=datetime.now()
                                 )

    # 全件取得
    for user in sekaoku_ctr.session.query(User).all():  # .all() は省略可
        print(user.id, user.name)

    for heritage in sekaoku_ctr.session.query(Heritage).all():
        print(heritage.id, heritage.name_en, heritage.name_jp,
              heritage.state_en, heritage.state_jp,
              heritage.longitude, heritage.latitude)

    for post in sekaoku_ctr.session.query(Post).all():
        print(post.id, post.user_id, post.heritage_id,
              post.type, post.image_full_url, post.image_thumbnail_url,
              post.date)

    sekaoku_ctr.close()


if __name__ == '__main__':
    main()

