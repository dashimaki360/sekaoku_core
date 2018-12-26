#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from sekaoku_table import Post, User, Heritage, Base


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

