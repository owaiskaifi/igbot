

import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = Your_Username
insta_password = Your_password 

dont_likes = [ 'vegan','food','religion' ]

#friends = ['list of friends I do not want to interact with']

like_tag_list = ['photography',   'cute',   
                    'pakistan' ]

# prevent posts that contain some plantbased meat from being skipped
#ignore_list = ['vegan', 'veggie', 'plantbased']

#accounts = ['accounts with similar content']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password
                 , headless_browser=True
                   )

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=10000)

    #session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
#    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=5, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 6),
                         amount=random.randint(50, 100), interact=True)

    #session.unfollow_users(amount=random.randint(75, 150),
    #                       InstapyFollowed=(True, "all"), style="FIFO",
    #                       unfollow_after=90 * 60 * 60, sleep_delay=501)

    """ Joining Engagement Pods...
    """
    photo_comments = ['lol',
        'lmao',
        'nicee' 
         ]

    session.set_do_comment(enabled = True, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')
    session.join_pods(topic='anime')
