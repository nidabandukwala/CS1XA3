# CS 1XA3 Project 03 - bandukwn

## Usage
- Activate conda environment using the command:
```python
conda activate djangoenv
```
- Run the project on the mac1xa3.ca server using the command:
```python
python manage.py runserver localhost:10012
```
- Run the project locally using the command:
```python
python manage.py runserver localhost:8000
```

  Note: Make sure you are in the directory that contains **manage.py** before running the command stated above.

In order to log in, enter the username: **'NB'** and the password: **'hello#1234'**.

All files can be accessed by the following path: **'CS1XA3/Project03**
## Objective 01: Login and Signup pages
#### Description:
- This feature is displayed in *signup.djhtml* rendered by *signup_view*. The HTML file is located in the *CS1XA3/Project03/login/templates* directory and the view is located in the *CS1XA3/Project03/login* directory.
- This feature can either be accessed by the url *mac1xa3.ca/e/bandukwn/signup/* **OR** by clicking on the "Create an account" button on the default login page.
- The signup page displays a form for creating an account. Once all the necessary details are entered into the form, the user is directly logged in and redirected to the Messages page of the website.
    - When the *Create an account* button is clicked, a POST request is sent which is handled by the **signup-view**.
    
    - The signup view is located in *CS1XA3/Project03/login* : **views.py** and uses the UserCreationForm as a template. After getting the username and password, a **UserInfo** object is created and the user is authenticated. If the authentication is successful, the user is automatically logged in and redirected to the messages page. 

## Objective 02: User Profile and Interests.
#### Description:
- This feature is displayed in *social_base.djhtml* located in the *CS1XA3/Project03/social/templates* directory. It makes use of the UserInfo model in *social/models.py* to display all attributes of the current user. The following code written under *messages_view*, *people_view*, and *account_view* gets all attributes of a user.
```python
user_info = models.UserInfo.objects.get(user=request.user)
```
- This feature can be accessed by the following URL:
          
          mac1xa3.ca/e/bandukwn/social/messages/
    The left hand side of the webpage displays all user information.
- The template *social_base.djhtml* displays the column used by *messages.djhtml, people.djhtml* and *account.djhtml*. This is why it has access to the respective views in *views.py*. 
- The HTML file makes use of django template variables to display properties of the current user. The following snippet of code shows how variables are used in the HTML file.
```python
{{ user_info.employment }}
{{ user_info.location }}
```
etc.
- Since a User can have multiple interests, a loop is used in the HTML file to display all interests of a user.
```python
{% for i in user_info.interests.all %}
..... {{ i.interests }}
{% endfor %}
```

## Objective 03: Account Settings Page.
#### Description:
- This feature is displayed in *CS1XA3/Project03/social/templates : account.djhtml* rendered by *CS1XA3/Project03/social : views.py : def account_view*. 
- It can either be accessed by clicking on the top right hand button on the navigation bar or by the following URL:

        mac1xa3.ca/e/bandukwn/social/account/

- This page displays a Password Change form and a form for updating User information.
- This view handles a POST request made by the user. It uses the in-built password change form as a template. Once the user is authenticated, all relevant details are updated and the user is redirected to the login page.
- The HTML file makes use of django template variables in order to display the form:
```python
<form method="post" id="form" action="{% url 'social:account_view' %}">
    {% csrf_token %}
    {{ form }}
    <input name="form" type="submit" value="Change Password"></input>
</form>
```
- The 'form' variable in the context of *account_view* is the one that is used in the HTML file.
- The Update Info form is rendered by *CS1XA3/Project03/social : views.py : def update_info*. It can be accessed in the same way as the password change form.
- This form works in the same way as the previous one. The HTML file makes use of the django template variable rendered in the context of the view and displays it:
```python
<form method="post" id="update_form" action="{% url 'social:update_info' %}">
    {% csrf_token %}
    {{ update_form }}
    <label for="employment">Employment: </label>
    <input id ="employment" type="text" name="employment"></input>
    ....
</form>
```
- The file *forms.py* located in the *CS1XA3/Project03/social* directory defines a Class for the form which deals with the information that has been inputted by the user. 

## Objective 04: Displaying People List.
#### Description:
- This feature is displayed in *CS1XA3/Project03/social/templates: people.djhtml* rendered by *CS1XA3/Project03/social : views.py : def people_view*. 
- It can be accessed by the following URL:

        mac1xa3.ca/e/bandukwn/social/people/

- *def people_view* loops over ALL users excluding the logged in user and appends those users to the **all_people list** who are not friends of the logged in user:
```python
user_info = models.UserInfo.objects.get(user=request.user)
users = models.UserInfo.objects.exclude(user=request.user)
all_people = []
for user in users:
    if user not in user_info.friends.all():
        all_people.append(user)

```
- The size of this list is limited using a session variable defined in the same file under *more_ppl_view*:
```python
x = request.session.get('counter',0)
request.session['counter'] = x+1
```
- The list:
```python
all_people[0:request.session.get('counter')]
```
- Under login_view in *CS1XA3/Project03/login : views.py*, the session variable is set to one so that it resets when the user logs in.  
- The HTML file makes use of django template variables to loop through the all_people list and display the username, employment, location and birthday of the users. 
```python
{% for i in all_people%}
..... {{ i.user.username}}
..... {{ i.employment }}
.....
{% endfor %}
```
- When the more button on the webpage is clicked, it sends an AJAX POST through javascript to *def more_ppl_view* which loads more people and reloads the page on success.
- The javascript file is located in *CS1XA3/Project03/social/static : people.js*.

## Objective 05: Sending Friend Requests
#### Description:
- This feature is displayed in *CS1XA3/Project03/social/templates : people.djhtml* rendered by *CS1XA3/Project03/social : views.py : def friend_request_view*. 
- The **Friend Request** buttons on the webpage are linked to a JQuery event in *CS1XA3/Project03/social/static : people.js*. When the button is clicked, the JQuery gets the id of the button and sends a POST request to **def friend_request_view**.
- This feature can be accessed by clicking on the "Friend Request" button in People. 
URL:

    mac1xa3.ca/e/bandukwn/social/people/

- The id of the button is given in the HTML file by:
```python
"fr-{{i.user_id}}"
```
which corresponds to the id of the user.
- The function in views.py uses the UserInfo model to get the username of the user who sent the request, and of the user to whom the request has been sent. 
- It then uses the FriendRequest model to create a new entry:
```python
some_user = models.UserInfo.objects.get(user_id=username)
x = models.UserInfo.objects.get(user=request.user)
models.FriendRequest.objects.create(to_user=some_user, from_user=x)
```
#### Exceptions:
- If the user is not authenticated, the page will automatically redirect to the login page.
- If the POST data does not contain any id, an **HttpResponseNotFound** error will be raised with the following error message
```
'friend_request_view called without frID in POST'
```
## Objective 06: Accepting/ Declining Friend Requests
#### Description:
- This feature is displayed in *CS1XA3/Project03/social/templates : people.djhtml* rendered by *CS1XA3/Project03/social : views.py : def accept_decline_view*. 
- The **Accept/Decline** buttons on the webpage are linked to a JQuery event in *CS1XA3/Project03/social/static : people.js*. When either button is clicked, the JQuery gets the id of the button and sends a POST request to **def accept_decline_view**.
- This feature can be accessed by clicking on either the "Accept" or the "Decline button in People.
URL:

    mac1xa3.ca/e/bandukwn/social/people/

- The id of the button is given in the HTML file by:
```python
"A-{{i.from_user.user_id}}"
```
corresponds to the id of the user who sent the request if the Accept button is clicked.
```python
"D-{{i.from_user.user_id}}"
```
which corresponds to the id of the user who sent the request if the Decline button is clicked.
- If the Accept button is clicked, the user who sent the request and to whom it was sent, the friends relation of both users are updated.
```python
y.friends.add(name1)
name1.friends.add(y) 
```
where y is the logged in user, and name1 is the user who sent the request.
- The corresponding FriendRequest entry is then deleted.

#### Exceptions:
- If the user is not authenticated, the page will automatically redirect to the login page.
- If the POST data does not contain any id, an **HttpResponseNotFound** error will be raised with the following error message
```
'accept_decline_view called without decision in POST'
```
## Objective 07: Displaying Friends
- This feature is displayed in *CS1XA3/Project03/social/templates : messages.djhtml* rendered by *CS1XA3/Project03/social : views.py : def messages_view*.
- This feature can be accessed by the following URL:
```
https://mac1xa3.ca/e/bandukwn/social/messages/
```
- The HTML file makes use of django template variables to loop over all friends of the logged in user and display their username:
```
{% for i in user_info.friends.all %}
{{ i.user.username }}
{% endfor %}
```
## Objective 08: Submitting Posts
#### Description:
- This feature is rendered by *CS1XA3/Project03/social : views.py : def post_submit_view*.
- The following URL can be used to view the content of the post:

    https://mac1xa3.ca/e/bandukwn/social/messages/

- The javascript file *messages.js* located in the *CS1XA3/Project03/social/static* sends an AJAX POST request to def post_submit_view when the "post" button is clicked. 
- The id of the button is used to get the content of the post which is then sent to the view.
```
json_data = {'postContent' : $('#post-text').text()}
```

- Once the post submission is handled, a new entry is added to the Post model:
```python
user_name = models.UserInfo.objects.get(user=request.user)
x=models.Post.objects.create(owner=user_name, content=postContent)
x.save()
```
- The page is then reloaded upon success.

#### Exceptions:
- If the user is not authenticated, the page will automatically redirect to the login page.
- If the POST data does not contain any id, an **HttpResponseNotFound** error will be raised with the following error message
```
'post_submit_view called without postContent in POST'
```

## Objective 09: Displaying Post List
#### Description:
- This feature is rendered by *CS1XA3/Project03/social : views.py : def messages_view*.
- It can be accessed by the following URL:

    https://mac1xa3.ca/e/bandukwn/social/messages/

- *def messages_view* loops over ALL the posts, sorts them from newest to oldest and appends them to a list called 'posts'
```python
user_info = models.UserInfo.objects.get(user=request.user)
users = models.Post.objects.all().order_by('-timestamp')
for i in users:
    posts.append(i)
```
- The size of this list is limited using a session variable defined in the same file under *more_post_view*:
```python
x = request.session.get('counter1',0)
request.session['counter1'] = x+1
```
- The list:
```python
posts[0:request.session.get('counter1')]
```
- Under login_view in *CS1XA3/Project03/login : views.py*, the session variable is set to one so that it resets when the user logs in.  
- The HTML file makes use of django template variables to loop through the posts list and display the name, time, and content of the post.
```python
{% for y in posts%}
{{ y.owner.user }}
{{ y.timestamp }}
{{ y.content }}
{% endfor %}
```
#### Exceptions:
- If the user is not authenticated, the page will automatically redirect to the login page.

## Objective 10: Liking Posts (and Displaying Like Count)
#### Description:
- This feature is displayed in *CS1XA3/Project03/social/templates : messages.djhtml* and rendered by *CS1XA3/Project03/social : views.py : def like_view*.
- It can be accessed by the following URL:

    https://mac1xa3.ca/e/bandukwn/social/messages/

- The like button is linked to a JQuery event located in *CSX1A3/Project03/social/static : messages.js*. Once the button is pressed, a POST request is sent to post_submit_view. The function then uses the UserInfo and the Post model to get the owner. It then updates the Post model by adding the user to the likes field:
```python
x = models.UserInfo.objects.get(user=request.user)
y= models.Post.objects.filter(owner=x)
var1 = models.Post.objects.get(pk=postidreq)
var1.likes.add(x)
```
- The id of the button is given in the HTML file by:
```python
"post-{{y.owner.user_id}}"
```
#### Exceptions:
- If the user is not authenticated, the page will automatically redirect to the login page.
- If the POST data does not contain any id, an **HttpResponseNotFound** error will be raised with the following error message
```
'like_view called without postID in POST'
```
## Objective 11: Test Database
#### User1:
- **Username** = "*NB*"
- **Password** = "*hello#1234*"
- **Employment** = "*Google*"
- **Location** = "*Hamilton*"
- **Birthday** = "*2000-12-12*"
- **Interests** = ["*Reading", "Art*"]
- **Friends** = ["*NRZ", "Ayez Sd", "Ash M, "JenK*"]

#### User2:
- **Username** = "*NRZ*"
- **Password** = "*helloo1*"
- **Employment** = "*Armani*"
- **Location** = "*Karachi, Pakistan*"
- **Birthday** = "*2000-11-09*"
- **Interests** = ["*Badminton", "Art*"]
- **Friends** = ["*NB", "Ayez Sd*"]

#### User3:
- **Username** = "*Ayez Sd*"
- **Password** = "*banana123*"
- **Employment** = "*AZ Corporation*"
- **Location** = "*Amsterdam, Netherlands*"
- **Birthday** = "*2000-09-10*"
- **Interests** = ["*Badminton", "Music*"]
- **Friends** = ["*NRZ", "NB", "Ash M, "Anj", "JenK*"]

#### User4:
- **Username** = "*Ash M*"
- **Password** = "*apple123*"
- **Employment** = "*Nestle*"
- **Location** = "*London, UK*"
- **Birthday** = "*2000-06-29*"
- **Interests** = ["*Baking", "Music*"]
- **Friends** = ["*NB", "Ayez Sd*"]

#### User5:
- **Username** = "*JenK*"
- **Password** = "*celery123*"
- **Employment** = "*Centre of Forensic Sciences, Toronto*"
- **Location** = "*Welland, Ontario*"
- **Birthday** = "*2001-06-14*"
- **Interests** = ["*Cooking", "Art*"]
- **Friends** = ["*NB", "Ayez Sd*"]

#### User6:
- **Username** = "*MJ*"
- **Password** = "*gym101*"
- **Employment** = "*Amazon*"
- **Location** = "*New York*"
- **Birthday** = "*2000-12-23*"
- **Interests** = ["*Badminton", "Hiking*"]
- **Friends** = ["*Ayesh K", "Yuv J*"]

#### User7:
- **Username** = "*Ayesh K*"
- **Password** = "*iateafork*"
- **Employment** = "*Microsoft*"
- **Location** = "*Mississauga, Ontario*"
- **Birthday** = "*2001-07-26*"
- **Interests** = ["*Reading", "Tennis*"]
- **Friends** = ["*MJ", "Yuv J*"]

#### User8:
- **Username** = "*Yuv J*"
- **Password** = "*dance12345*"
- **Employment** = "*P&G*"
- **Location** = "*Indore, India*"
- **Birthday** = "*2002-02-18*"
- **Interests** = ["*Biking", "Cooking*"]
- **Friends** = ["*MJ", "Ayesh K*"]

#### User9:
- **Username** = "*Anj*"
- **Password** = "*ilostmykeys*"
- **Employment** = "*Apple*"
- **Location** = "*Mississauga, Ontario*"
- **Birthday** = "*2001-10-26*"
- **Interests** = ["*Baking", "Art*"]
- **Friends** = ["*Ayez Sd*"]
