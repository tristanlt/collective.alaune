from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class ALaUne(ViewletBase):
    render = ViewPageTemplateFile('ALaUne.pt')
    def update(self):
        newsontopFolderId = self.context.id+'-alaune'
        try:
            newsontopFolder = self.context[newsontopFolderId]
        except:
            self.activate=False
        else:
            self.activate=True
            self.title = newsontopFolder.title
            self.description = newsontopFolder.Description
            self.newsObj=newsontopFolder.listFolderContents(contentFilter={"portal_type" : "News Item"})