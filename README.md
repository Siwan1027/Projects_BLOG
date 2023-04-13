# Blog with Animal Crossing wiki

<img src="https://blog.kakaocdn.net/dn/6Yr5Z/btqCymfM6RQ/bqyCiPRsnRClX3bN7TymK0/img.png" width="50px" height="50px" title="AnimalCrossing_Logo"/>

## Models

### User[AbstractUser]
- required info
    1. username
    2. password
<<<<<<< HEAD
    3. like_postings(MtoM)
    4. follow(MtoM)
    5. caught(MtoM)
=======
    3. like_postings
    4. follow
>>>>>>> parent of e03dccb (Update README.md)
### Posting
- required info
    1. title
    2. content
    3. created_at
    4. updated_at
    5. user(FK)
### reply
- required info
    1. content
    2. created_at
    3. updated_at
    4. user(FK)
    5. poating(FK)
## forms

### UserForm
- auth
    1. username
### PostingForm
- auth
    1. title
    2. password
### ReplyForm
- auth
    1. content

## templates

### base
#### navbar
- icon 
    - to index
- positings
    - show all posting
        - paginating by 10 postings
- now available
    - show all fishes, bugs, sea creatures order by price
- dict
    - show all the informations that fits each section
    - sections
        - fishes
        - bugs
        - sea creatures
        - fossils
        - furnitures
        - villagers
        - events

#### sidebar
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
        - button for signin
        - button for signup
#### block content

#### footer
- icon
    - GitHub
- Github
    - 'www.github.com/{user.GitHubID}
- nookipedia
    - 'www.nookipedia.com'

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
    - show 10 fishes can caught in now

### signup
- show signup form

### signin
- show signin form

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