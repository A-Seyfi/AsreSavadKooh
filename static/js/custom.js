function sendArticleComment(articleId) {
    var comment = $('#commentText').val();
    // console.log(comment);
    if (comment) {
        $.get('add-article-comment', {
            article_comment: comment,
            article_id: articleId
        }).then(res => {
            console.log(res);
            location.reload();
        });
    }
}
