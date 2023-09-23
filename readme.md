# Google API Learn

This is a project I created while learning how to use Google's API

## Setup

1. Create a project in Google Cloud
2. In that project, create credentials that are permitted to access the Photos Library API
3. Allow redirect URL of `http://localhost:5500/`
4. Set up your python environment as you desire and `pip install -r requirements.txt`

## Usage

To get credentials, run
```shell
python auth.py
```

To get an album ID, edit `list-library.py` to call `list_albums()` and run it. Once you have your album ID, edit
`list-library.py` to call `list_album_contents()` again and run
```shell
export GOOGLE_ALBUM_ID=your-album-id
python list-library.py
```
