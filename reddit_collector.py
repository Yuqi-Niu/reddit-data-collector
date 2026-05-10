import praw
import pandas as pd
from datetime import datetime, timezone

from config import (
    CLIENT_ID,
    CLIENT_SECRET,
    USER_AGENT,
    SUBREDDITS,
    POST_LIMIT,
    COLLECT_COMMENTS,
    COMMENT_LIMIT_PER_POST,
    SORT_TYPE,
    KEYWORD,
    OUTPUT_POSTS_FILE,
    OUTPUT_COMMENTS_FILE,
)


def utc_to_readable_time(created_utc):
    return datetime.fromtimestamp(
        created_utc,
        tz=timezone.utc
    ).strftime("%Y-%m-%d %H:%M:%S")


def create_reddit_client():
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
    )


def get_posts(subreddit, sort_type, limit, keyword=None):
    if keyword:
        return subreddit.search(keyword, sort=sort_type, limit=limit)

    if sort_type == "hot":
        return subreddit.hot(limit=limit)
    elif sort_type == "top":
        return subreddit.top(limit=limit)
    elif sort_type == "rising":
        return subreddit.rising(limit=limit)
    elif sort_type == "controversial":
        return subreddit.controversial(limit=limit)
    else:
        return subreddit.new(limit=limit)


def collect_posts_and_comments():
    reddit = create_reddit_client()

    all_posts = []
    all_comments = []

    for subreddit_name in SUBREDDITS:
        print(f"\nCollecting posts from r/{subreddit_name}...")

        subreddit = reddit.subreddit(subreddit_name)
        posts = get_posts(
            subreddit=subreddit,
            sort_type=SORT_TYPE,
            limit=POST_LIMIT,
            keyword=KEYWORD,
        )

        for post in posts:
            post_data = {
                "post_id": post.id,
                "subreddit": subreddit_name,
                "title": post.title,
                "text": post.selftext,
                "author": str(post.author) if post.author else None,
                "score": post.score,
                "upvote_ratio": post.upvote_ratio,
                "num_comments": post.num_comments,
                "created_utc": post.created_utc,
                "created_time_utc": utc_to_readable_time(post.created_utc),
                "url": post.url,
                "permalink": f"https://www.reddit.com{post.permalink}",
                "is_self": post.is_self,
                "over_18": post.over_18,
                "spoiler": post.spoiler,
                "locked": post.locked,
            }

            all_posts.append(post_data)

            if COLLECT_COMMENTS:
                print(f"  Collecting comments for post: {post.id}")

                post.comments.replace_more(limit=0)

                comment_count = 0

                for comment in post.comments.list():
                    if comment_count >= COMMENT_LIMIT_PER_POST:
                        break

                    comment_data = {
                        "comment_id": comment.id,
                        "post_id": post.id,
                        "subreddit": subreddit_name,
                        "body": comment.body,
                        "author": str(comment.author) if comment.author else None,
                        "score": comment.score,
                        "created_utc": comment.created_utc,
                        "created_time_utc": utc_to_readable_time(comment.created_utc),
                        "parent_id": comment.parent_id,
                        "link_id": comment.link_id,
                        "permalink": f"https://www.reddit.com{comment.permalink}",
                    }

                    all_comments.append(comment_data)
                    comment_count += 1

    return all_posts, all_comments


def save_to_csv(posts, comments):
    posts_df = pd.DataFrame(posts)
    posts_df.to_csv(
        OUTPUT_POSTS_FILE,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nSaved {len(posts_df)} posts to {OUTPUT_POSTS_FILE}")

    if COLLECT_COMMENTS:
        comments_df = pd.DataFrame(comments)
        comments_df.to_csv(
            OUTPUT_COMMENTS_FILE,
            index=False,
            encoding="utf-8-sig"
        )

        print(f"Saved {len(comments_df)} comments to {OUTPUT_COMMENTS_FILE}")


def main():
    posts, comments = collect_posts_and_comments()
    save_to_csv(posts, comments)
    print("\nDone!")


if __name__ == "__main__":
    main()