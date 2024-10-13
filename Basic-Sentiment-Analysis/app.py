from textblob import TextBlob

comments = [
    "I love the way manhwa stories are told; they are so unique!",
    "Manga will always be superior to manhwa, no competition.",
    "Manhwa has such vibrant colors compared to manga, it's amazing!",
    "I don't like how some manhwas are too short, they feel rushed.",
    "Manga has more detailed art, which I prefer over manhwa.",
    "Manhwa webtoons are really engaging and easy to read on my phone.",
    "Not a fan of manhwa; it's just not as good as traditional manga.",
    "Both manga and manhwa have their charm, but I enjoy them equally.",
    "The art style in manhwa is incredible; I can't get enough of it!",
    "Manga's plot depth is something manhwa can't match, in my opinion.",
    "I love reading manhwa for its vibrant visuals and short chapters.",
    "Manga feels more classic and grounded compared to manhwa.",
    "Manhwa's storytelling has a fresh perspective I really enjoy.",
    "Some manhwa series are so creative and innovative, it's refreshing.",
    "I wish manhwa had longer episodes like traditional manga."
]

def classify_comment_sentiment(comment):
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return "positive"
    else:
        return "negative"

results = [classify_comment_sentiment(comment) for comment in comments]

positive_count = results.count("positive")
negative_count = results.count("negative")

total_comments = len(comments)
positive_percentage = (positive_count / total_comments) * 100
negative_percentage = (negative_count / total_comments) * 100

print(f"Total comments analyzed: {total_comments}")
print("The Analysis of comments for 'The Difference Between Manga and Manhwa' says")
print(f"Positive comments: {positive_percentage:.2f}%")
print(f"Negative comments: {negative_percentage:.2f}%")
