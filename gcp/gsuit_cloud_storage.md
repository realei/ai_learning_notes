1. On the Google Cloud Platform menu, click Activate Cloud Shell Activate Cloud Shell. If a dialog box appears, click Continue.

2. For convenience, enter your chosen location into an environment variable called LOCATION. Enter one of these commands:

`export LOCATION=EU`

3. In Cloud Shell, the DEVSHELL_PROJECT_ID environment variable contains your project ID. Enter this command to make a bucket named after your project ID

`gsutil mb -l $LOCATION gs://$DEVSHELL_PROJECT_ID`

If prompted, click Authorize to continue.

4. Retrieve a banner image from a publicly accessible Cloud Storage location:

`gsutil cp gs://cloud-training/gcpfci/my-excellent-blog.png my-excellent-blog.png`

5. Copy the banner image to your newly created Cloud Storage bucket:

`gsutil cp my-excellent-blog.png gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png`

6. Modify the Access Control List of the object you just created so that it is readable by everyone:

`gsutil acl ch -u allUsers:R gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png`
