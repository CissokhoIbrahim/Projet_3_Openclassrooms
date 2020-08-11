"""file for objects"""
class Objects:
    """docstring for objects"""
    def __init__(self, custom_count=0):
        """the methode initt for objects"""
        self.custom_count = custom_count
        self.items = {
            't' : True,
            'e' : True,
            's' : True
            }



    def add(self):
        """ function get objects"""
        items_choice = ""
        if items_choice == 't' and self.items['t' : True]:
            self.custom_count += 1
            return True
        if items_choice == 'e' and self.items['e' : True]:
            self.custom_count += 1
            return True
        if items_choice == 's' and self.items['s' : True]:
            self.custom_count += 1
            return True
        return False

if __name__== "__main__":

    o = Objects()
