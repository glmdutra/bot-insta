"""RELEASE

https://pypi.org/project/instapy/0.1.0/
https://pysimplegui.readthedocs.io/en/latest/
https://pypi.org/project/selenium/
https://github.com/mozilla/geckodriver/releases


INSTALL INSTAPY: pip install instapy
INSTAL PYSIMPLEGUI: pip install pysimplegui

"""


from instapy import InstaPy

session = InstaPy(username="zshoes.store", password="36980293")
session.login()

session.follow_likers(['netshoes', 'kanuibr'], photos_grab_amount = 5, follow_likers_per_photo = 5, randomize = True, sleep_delay = 600, interact = False)
session.follow_commenters(['netshoes', 'kanuibr'], amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=False)

session.end()