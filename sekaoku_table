#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.ext import declarative
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

Base = declarative.declarative_base()


class Post(Base):
    """
    post table class
    """
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    heritage_id = Column(Integer, nullable=False)
    image_full_url = Column(String, nullable=False)
    image_thumbnail_url = Column(String, nullable=False)
    comment = Column(String)
    check = Column(Integer)
    likes = Column(Integer)
    date = Column(DateTime, nullable=False)


class User(Base):
    """
    user table  class
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    first_post_date = Column(DateTime)
    twitter_id = Column(String)


class Heritage(Base):
    """
    world heritage table  class
    """
    __tablename__ = 'heritages'

    id = Column(Integer, primary_key=True)
    name_en = Column(String, nullable=False)
    name_jp = Column(String, nullable=False)
    state_en = Column(String, nullable=False)
    state_jp = Column(String, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)


def main():
    # DB 設定の動作確認メソッド
    # データベースとの接続に使う情報
    # ここでは SQLite のオンメモリデータベースを使う
    # echo=True とすることで生成される SQL 文を確認できる
    engine = create_engine('sqlite:///', echo=True)
    # モデルの情報を元にテーブルを生成する
    Base.metadata.create_all(engine)
    # データベースとのセッションを確立する
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # データベースのトランザクションを作る
    with session.begin(subtransactions=True):
        # add user
        for i in range(5):
            user = User(name='Alice')
            session.add(user)

        # add heritage
        for i in range(5):
            heritage = Heritage(name_en='Mt Fuji',
                                name_jp='富士山',
                                state_en='japanese highest mountain',
                                state_jp='日本一高い山',
                                longitude=35.360556,
                                latitude=138.727778
                                )
            session.add(heritage)

        # add post
        for i in range(5):
            post = Post(user_id=i+1, heritage_id=i+1,
                        type="place",
                        image_full_url="http://sample_image.com",
                        image_thumbnail_url="http://sample_thumbnail_image.com",
                        date=datetime.now())
            session.add(post)

    # 全件取得
    for user in session.query(User).all():  # .all() は省略可
        print(user.id, user.name)

    for heritage in session.query(Heritage).all():
        print(heritage.id, heritage.name_en, heritage.name_jp,
              heritage.state_en, heritage.state_jp,
              heritage.longitude, heritage.latitude)

    for post in session.query(Post).all():
        print(post.id, post.user_id, post.heritage_id,
              post.type, post.image_full_url, post.image_thumbnail_url,
              post.date)


if __name__ == '__main__':
    main()

