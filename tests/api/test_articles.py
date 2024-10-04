#
# Article Tests
#


def test_get_articles(client, add_user, add_article):
    user = add_user()
    articles = [
        add_article(author_user_id=user["id"]) for _ in range(3)
    ]

    resp = client.get("/api/articles")
    assert resp.status_code == 200
    assert len(resp.json["articles"]) == len(articles)

    # Ensure the articles are in most recent order
    for idx, article in enumerate(reversed(articles)):
        assert resp.json["articles"][idx] == {
            "slug": article["slug"],
            "title": article["title"],
            "description": article["description"],
            "body": article["body"],
            "tagList": article["tags"],
            "createdAt": article["created_date"],
            "updatedAt": article["updated_date"],
            "favorited": False,
            "favoritesCount": 0,
            "author": {
                "username": user["username"],
                "bio": user["bio"],
                "image": user["image"],
                "following": False,
            },
        }


# @pytest.mark.skip("Requires authentication.")
# def test_get_feed(client, add_user, add_article):
#     user = add_user()
#     article = add_article(author_user_id=user["id"])
#     # TODO: Authenticate as the user before making the request
#     resp = client.get("/api/articles/feed")
#     assert resp.status_code == 200
#     assert resp.json["articles"][0]["slug"] == article["slug"]


# def test_get_article(client, add_article):
#     article = add_article()
#     resp = client.get(f"/api/articles/{article['slug']}")
#     assert resp.status_code == 200
#     assert resp.json["article"]["slug"] == article["slug"]


# @pytest.mark.skip("Requires authentication.")
# def test_create_article(client, add_user):
#     user = add_user()
#     # TODO: Authenticate as the user before making the request
#     payload = {
#         "article": {
#             "title": "How to Article",
#             "description": "A test article.",
#             "body": "This is just a test!",
#             "tagList": ["test", "article"],
#         }
#     }
#     resp = client.post("/api/articles", json=json.dumps(payload))
#     assert resp.status_code == 200
#     assert resp.json["article"]["title"] == payload["article"]["title"]


# @pytest.mark.skip("Requires authentication.")
# def test_update_article(client, add_user, add_article):
#     user = add_user()
#     article = add_article(author_user_id=user["id"])
#     # TODO: Authenticate as the user before making the request
#     payload = {
#         "article": {
#             "title": "Updated Article",
#             "description": "An updated test article.",
#             "body": "This is an updated test!",
#             "tagList": ["updated", "article"],
#         }
#     }
#     resp = client.put(f"/api/articles/{article['slug']}", json=json.dumps(payload))
#     assert resp.status_code == 200
#     assert resp.json["article"]["title"] == payload["article"]["title"]


# @pytest.mark.skip("Requires authentication.")
# def test_delete_article(client, add_user, add_article):
#     user = add_user()
#     article = add_article(author_user_id=user["id"])
#     # TODO: Authenticate as the user before making the request
#     resp = client.delete(f"/api/articles/{article['slug']}")
#     assert resp.status_code == 200
#     # TODO: Add a check to ensure the article was actually deleted


# #
# # Article Favorties Tests
# #
# @pytest.mark.skip("Requires authentication.")
# def test_favorite_article(client, add_user, add_article):
#     user = add_user()
#     article = add_article()
#     # TODO: Authenticate as the user before making the request
#     resp = client.post(f"/api/articles/{article['slug']}/favorite")
#     assert resp.status_code == 200
#     assert resp.json["article"]["favorited"] == True


# @pytest.mark.skip("Requires authentication.")
# def test_unfavorite_article(client, add_user, add_article, add_article_favorite):
#     user = add_user()
#     article = add_article()
#     add_article_favorite(user_id=user["id"], article_id=article["id"])
#     # TODO: Authenticate as the user before making the request
#     resp = client.delete(f"/api/articles/{article['slug']}/favorite")
#     assert resp.status_code == 200
#     assert resp.json["article"]["favorited"] == False


# #
# # Article Comments Tests
# #
# def test_get_comments(client, add_article, add_article_comment):
#     article = add_article()
#     comment = add_article_comment(article_id=article["id"])
#     resp = client.get(f"/api/articles/{article['slug']}/comments")
#     assert resp.status_code == 200
#     assert resp.json["comments"][0]["id"] == comment["id"]


# @pytest.mark.skip("Requires authentication.")
# def test_create_comment(client, add_user, add_article):
#     user = add_user()
#     article = add_article()
#     # TODO: Authenticate as the user before making the request
#     data = {"comment": {"body": "What a nice article!"}}
#     resp = client.post(
#         f"/api/articles/{article['slug']}/comments", json=json.dumps(data)
#     )
#     assert resp.status_code == 200
#     assert resp.json["comment"]["body"] == data["comment"]["body"]


# @pytest.mark.skip("Requires authentication.")
# def test_delete_comment(client, add_user, add_article, add_article_comment):
#     user = add_user()
#     article = add_article()
#     comment = add_article_comment(
#         article_id=article["id"], commenter_user_id=user["id"]
#     )
#     # TODO: Authenticate as the user before making the request
#     resp = client.delete(f"/api/articles/{article['slug']}/comments/{comment['id']}")
#     assert resp.status_code == 200
#     # TODO: Add a check to ensure the comment was actually deleted


# #
# # Article Comments Tests
# #
# def test_get_tags(client, add_article):
#     add_article(tags=["mock"])
#     add_article(tags=["test", "article"])

#     resp = client.get("/api/tags")
#     assert resp.status_code == 200
#     assert resp.json["tags"] == [
#         "mock",
#         "test",
#         "article",
#     ]
