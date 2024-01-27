# User Registration
  It is the process of creating user account in any website or application where the application collecting the user details
# Django Provides secure authentication system to handle user realted functionality
# User registration process in DJango
User Model:
Django comes with a built-in User model (django.contrib.auth.models.User) that includes fields like username, email, and password.
In modern Django versions (after 1.11), it's recommended to use the AbstractUser model for customizing user models.

so you no need to create a model which is responsible to define username, pswd, email. While creating the the form for User model you need to 
specify the fields in fields list in order to make more specific as built-in user model contains more no.of fields.

## if your form is taking image files or any kind of files then you need to create a directory for storing that collected files i.e media(directory in outer project folder
## and need to specify MEDIA_ROOT variable externally for storing path of media directory
# STATIC_ROOT : 
  In settings Django by default specifies that STATIC_ROOT= 'static/'
  Is a directory where Django should collect all the satic files of various applications into a single location 
# MEDIA_ROOT :
  In settings, you need to define MEDIA_ROOT variable like MEDIA_ROOT='media/'
  Is a directory where media files are connected.
# Collect submitted Data and then modify password field to make it need to be as encrypt and then save
# Here in the template, along with the method attribute, you have to specify enctype='multipart/form-data'


