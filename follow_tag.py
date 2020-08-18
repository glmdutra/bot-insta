from instapy import InstaPy

session = InstaPy(username="zshoes.store", password="36980293", headless_browser=True)
session.login()

# Curtir publicações seguindo a referência de tags;
session.like_by_tags(["Calçado", "tênis", "t-shirts", "shoes", "tênis nike"], amount=5)
session.set_dont_like(["naked", "nsfw", "rape", "violence", "suicide"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

session.end()