'''Contains all functions used by finishing_status()'''

class FinishingStatus():
    '''Contains all methods used to get the finishing status info'''
    def __init__(self, results):
        self.results = results
    def get_status_id(self):
        '''Returns status id for each status'''
        return [i["statusId"] for i in self.results]
    def get_status(self):
        '''Returns the status values or info'''
        return [i["status"] for i in self.results]
    def get_status_count(self):
        '''Returns the count for each status info'''
        return [i["count"] for i in self.results]
