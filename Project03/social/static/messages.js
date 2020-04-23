/* ********************************************************************************************
   | Handle Submitting Posts - called by $('#post-button').click(submitPost)
   ********************************************************************************************
   */
function submitPost(event) {
    let json_data = {'postContent' : $('#post-text').text()};
    console.log($('#post-text').text());
    let url_path = post_submit_url;
    //print (status)
    // TODO Objective 8: send contents of post-text via AJAX Post to post_submit_view (reload page upon success)
    $.post(url_path,
           json_data,
           moreResponse);
   if (status == 'success') {
       location.reload();
   }
}

/* ********************************************************************************************
   | Handle Liking Posts - called by $('.like-button').click(submitLike)
   ********************************************************************************************
   */
function submitLike(event) {
    let postID = this.id;
    console.log(postID)
    let json_data = {'postID' : postID };
    let url_path = like_post_url;
    $.post(url_path,
           json_data,
           moreResponse);
    if (status == 'success') {
       location.reload();
   }
    // TODO Objective 10: send post-n id via AJAX POST to like_view (reload page upon success)
}

/* ********************************************************************************************
   | Handle Requesting More Posts - called by $('#more-button').click(submitMore)
   ********************************************************************************************
   */
function moreResponse(data,status) {
    if (status == 'success') {
        // reload page to display new Post
        location.reload();
    }
    else {
        alert('failed to request more posts' + status);
    }
}

function submitMore(event) {
    // submit empty data
    let json_data = { };
    // globally defined in messages.djhtml using i{% url 'social:more_post_view' %}
    let url_path = more_post_url;

    // AJAX post
    $.post(url_path,
           json_data,
           moreResponse);
}

/* ********************************************************************************************
   | Document Ready (Only Execute After Document Has Been Loaded)
   ********************************************************************************************
   */
$(document).ready(function() {
    // handle post submission
    $('#post-button').click(submitPost);
    // handle likes
    $('.like-button').click(submitLike);
    // handle more posts
    $('#more-button').click(submitMore);
});
