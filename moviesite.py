import webbrowser

class Movies:
    def __init__(self,m_title,m_story,m_image,m_trailer):
        self.title=m_title
        self.storyline=m_story
        self.poster_image_url=m_image
        self.trailer_youtube_url=m_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
