from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib import messages
from . import models
from . import forms
from .models import UserInfo
from social.forms import UpdateInfo
def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        posts = []
        user_info = models.UserInfo.objects.get(user=request.user)
        users = models.Post.objects.all().order_by('-timestamp')
        for i in users:
            posts.append(i)



        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post

        context = { 'user_info' : user_info
                  , 'posts' : posts[0:request.session.get('counter1')]
                  }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    if request.user.is_authenticated:
        form = None


        # TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password
    if request.method == 'POST':
             form = PasswordChangeForm(request.user, request.POST)
             if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                request.session['failed'] = False
                return redirect('login:login_view')


    else:
         form = PasswordChangeForm(request.user)


    user_info = models.UserInfo.objects.get(user=request.user)
    context = { 'user_info' : user_info,
                    'form' : form
                       }
    return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def update_info(request):
     if request.method == 'POST':
           update_form = forms.UpdateInfo(request.user, request.POST)
           if update_form.is_valid():
               user = update_form.save()
               employment = update_form.cleaned_data['employment']
               location = update_form.cleaned_data['location']
               birthday = update_form.cleaned_data['birthday']
               interests = update_form.cleaned_data['interests']
               update_session_auth_hash(request,user)
               request.session['failed'] = False
               return redirect('social:messages_view')
     else:
           update_form = forms.UpdateInfo(request.user)

     user_info = models.UserInfo.objects.get(user=request.user)
     context = { 'user_info' : user_info,
                 'update_form' : update_form
                     }
     return render(request, 'account.djhtml', context)

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        users = models.UserInfo.objects.exclude(user=request.user)
        all_people = []
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
        for user in users:
               if user not in user_info.friends.all():
                  all_people.append(user)


        # TODO Objective 5: create a list of all friend requests to current user
        friend_requests = []
        x = models.FriendRequest.objects.filter(to_user=user_info)
        print(x)
        for i in x:
               friend_requests.append(i)

        context = { 'user_info' : user_info,
                    'all_people' : all_people[0:request.session.get('counter')],
                    'friend_requests' : friend_requests }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    print(postIDReq)
    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = 0
        postid = postIDReq[5:]
        postidreq = int(postid)

        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field
            x = models.UserInfo.objects.get(user=request.user)
            y= models.Post.objects.filter(owner=x)
            var1 = models.Post.objects.get(pk=postidreq)
            var1.likes.add(x)
            status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    print(postContent)
    if postContent is not None:
        if request.user.is_authenticated:

            # TODO Objective 8: Add a new entry to the Post model
            user_name = models.UserInfo.objects.get(user=request.user)
            x=models.Post.objects.create(owner=user_name, content=postContent)
            x.save()

            #return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed

        # TODO Objective 9: update how many posts are displayed/returned by messages_view
        x = request.session.get('counter1', 0)
        request.session['counter1'] = x+3

        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed
        x = request.session.get('counter',0)
        request.session['counter'] = x+1

        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''

    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]

        if request.user.is_authenticated:
            # TODO Objective 5: add new entry to FriendRequest
            some_user = models.UserInfo.objects.get(user_id=username)
            x = models.UserInfo.objects.get(user=request.user)
            models.FriendRequest.objects.create(to_user=some_user, from_user=x)

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    if data is not None:
        username = data[2:]
        # TODO Objective 6: parse decision from data

        if request.user.is_authenticated:
            name1 = models.UserInfo.objects.get(user_id=username)
            y = models.UserInfo.objects.get(user=request.user)
            x = models.FriendRequest.objects.get(from_user=name1, to_user=y)
            if data[:2] == "A-":
                y.friends.add(name1)
                name1.friends.add(y)
            x.delete()

            # TODO Objective 6: delete FriendRequest entry and update friends in both Users

            status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
