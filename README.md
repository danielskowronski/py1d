# py1d
Python OneDrive [Py1d] - simple command line client for MS OneDrive.

### technology
Python 3 with requests library + server side PHP

### features
 + user tokens generation wizard (full graphical web browser needed to login to MS account)
 + file upload (currently to root directory only)
 + account info

### todo
 + file download
 + directory support
 + next version: OneDrive for Business

### current usability status
ready to be used as simple uploader

### how to use it
developer needs to create application on https://account.live.com/developers/applications/index (sadly there is no api for single user use); app id should be stored in _api_client_id and secret key in _api_secret_key

there is also need te retreive token from callback - easiest way is to put simple PHP file that will echo back POST data for user to copy-paste (see liveapi.php); this should be configured via _api_callback_url

### docs
https://msdn.microsoft.com/en-us/library/hh826521.aspx -- general API docs

### notes
currently there is no support for "OneDrive for Business" / SharePoint Disk - the one you get by logging in by organizational credentials (eg. university's) but it will be soon implemented
