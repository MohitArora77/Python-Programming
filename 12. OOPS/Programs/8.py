#Take a library.
class lib:
    lname="St.Peterson lib"
    lloc="London,UK"
    lcon=3646237689
    
    def __init__(self,b_name,b_no,b_genre,b_author):
        self.b_name=b_name
        self.b_no=b_no
        self.b_genre=b_genre
        self.b_author=b_author
    
    def disp_obj(self):
        print(self.b_name,self.b_no,self.b_genre,self.b_author)
    
    def ch_b_no(self,new):
        self.b_no=new
        
TheAlchemist=lib("TheAlchemist",5436,"Supernatural","Paulo Coelho")
Pilgrimage=lib("Pilgrimage",4567,"Adventure","Paulo Coelho")
who_will_cry_when_u_die=lib("Who will cry when u die",6788,"Thriller","Robin")

TheAlchemist.disp_obj()
TheAlchemist.ch_b_no(7896)
TheAlchemist.disp_obj()




