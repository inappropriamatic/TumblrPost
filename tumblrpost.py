#!/usr/bin/python
## INAPPROPRIAMATIC
## inappropriamatic.tumblr.com 
import httplib, urllib


"""A class for uploading to tumblr.

Currently only supports photos, because that is all I am interested in."""

class TumblrPost():
    
    def __init__(self, email=None, password=None, up_file=None):
        self.tumblr_url = "tumblr.com"
        self.api_path   = "/api/write"
        
        self.email = email
        self.password = password
        
        self.sub_type  = "photo"
        self.sub_group = None
        self.sub_state = None    
        
        self.up_file = up_file  # the file to post
    
        self.caption = ""
        
    def set_credentials(self, email, password):
        """Set a user name and password to log into Tumblr with."""
        self.email = email
        self.password = password
    
    
    def set_submission(self, up_file, sub_type, sub_group, sub_state):
        """Set the file to be uploaded, the type of submission, the group to 
        submit it in, and the state which it should be uploaded in.
        
        
        up_file - The path to the file to be uploaded
        sub_type - The type of post: regular, photo, quote, link, converstation, video, audio
        sub_group - Post to a secondary tumblr on your account
        sub_state - The submission state: published, draft, submission, queue"""
        
        self.up_file = up_file
        self.sub_type = sub_type
        self.sub_group = sub_group
        self.sub_state = sub_state
    


    def set_upload_file(self, up_file):
        """Takes a path to a file to be uploaded"""
        self.up_file = up_file


    def set_caption(self, caption):
        self.caption = caption

    def set_state(self, state):
        self.sub_state = state
        

    def connect_and_post(self):
        """Connect to tumblr and send an image in an http POST.  Max file size 5mb"""
        image = open(self.up_file)
        params = urllib.urlencode({'email': self.email,
                                   'password': self.password,
                                   'type': self.sub_type,
                                   #'group': self.sub_group,
                                   'state': self.sub_state,
                                   #'click-through-url' : self.sub_group,
                                   'data': image.read(),
                                   'caption': self.caption
                                       })
        
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
                   
        conn = httplib.HTTPConnection(self.tumblr_url, 80)
        conn.request("POST", self.api_path, params, headers)
        response = conn.getresponse()

        conn.close()
        return response.status == 201
    
