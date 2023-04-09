# Blog

## Models

### User
- required info
    1. username
    2. password
    3. GitHub ID
### Posting
- required info
    1. title
    2. content
    3. created_at
    4. updated_at
### reply
- required info
    1. content
    2. created_at
    3. updated_at
## forms

### UserForm
- auth
    1. all
### PostingForm
- auth
    1. title
    2. password
### reply
- auth
    1. content

## templates

### base
#### navbar
- icon 
    - to index
#### sidebar_l
- userinfo
    - show if logged in
        - username
            - direct to userdetail
        - number of posts
        - number of replies
        - number of followers
        - number of followings
        - button for write new posting
            - direct to create.html
    - show if not logged in
        - show login bars
        - button for login
#### block content

#### footer
- icon
    - GitHub
- Github
    - 'www.github.com/{user.GitHubID}

### create
- create[for only logged in user]
    - show text area for write new posting
    - buttons
        - submit
            - if authrized
                - save()
            - else
                - redirect to create.html
        - cancle
            - redirect to index

### detail
- detail
    - show title
    - show updated time
    - show writer
        - direct to user info
    - show detail of specific posting
        - show buttons if posting_user == request_user
            1. modify
            2. delete
        - show buttons if posting_user != request_user
            1. like
    - input type text for write reply

### index
- index
    - show 5 postings most liked

### signup
- show userform.as_p

### userdetail
- userpostings with titles
    - redirect to detail
- userpostings with contents in 20 letters
    - redirect to detail
- show followers, followings
- if request.username != login.user
    - show follow/unfollow btn


## DB relationships

1. Postings.FK -> User.PK
2. Reply.FK -> Posting.PK, User.PK
3. follow <-> User
4. like <-> User