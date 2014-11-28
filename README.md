Stevens-Bazaar
==============

Shared economy based online portal to buy, sell or rent stuff for student community.
This website has been developed using python, HTML, CSS, Javascript.
Django is the MTV framework used.

main_page : This is the project with all the details of the apps, database, static file settings.
signin    : This is the app for home page (home), registration (register_user), login (login), 
            logout (logout), authentication (auth_view), aboutus (aboutus), faqs (FAQs), team (team), 
            terms of use (terms) and other validations (register_success, invalid_email, firsttime, 
            invalid_login, loggedin). Refer views.py for details on the logic. 
            Refer forms.py for modification to registration form per our usage. 
            We are validating if the email id is valid college email id before allowing user to register.
         
post      : This is the app to post an advertisement (adpost), search an advertisement (search) (Details 
            are mentioned in views.py about the search logic), view advertisement (posts_view). 
            
            
For more details on the search logic, please refer the below link:
http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap

For help with coding using python django the below youtube videos are very helpful.

CodingEntrepreneurs : http://www.youtube.com/channel/UCWEHue8kksIaktO8KTTN_zg
Mike Hibbert        : http://www.youtube.com/user/MickeySoFine1972

For documentation on django and installation refer the below links:
https://docs.djangoproject.com/en/1.6/contents/
http://www.djangobook.com/en/2.0/index.html
