import smartpy as sp

class Storage(sp.Contract):
    def __init__(self):
        self.init(
            my_List = [],
            user  = sp.map({},tkey=sp.TAddress,tvalue=sp.list([],t=sp.TString)),
            # access_by_user = sp.map({},tkey=sp.TAddress,tvalue=sp.map({},tkey=sp.TAddress,tvalue=sp.TBool)),
            # access_list = sp.map({},tkey=sp.TAddress,tvalue=sp.map({},tkey=sp.TAddress,tvalue=sp.TBool)),
            # list = sp.map({},tkey=sp.TAddress,tvalue=sp.TBool),
            # # access_list = sp.map({},tkey=sp.TAddress,tvalue=sp.TList(Access)),
            # previous_data = sp.map({},tkey=sp.TAddress,tvalue=sp.map({},tkey=sp.TAddress,tvalue=sp.TBool)),    
        )

    @sp.entry_point
    def add(self,url):
        sp.set_type(url,sp.TString)
        self.data.my_list.push(url)
        self.data.user=sp.map({sp.sender:self.data.my_list})
       

@sp.add_test(name="Storage")
def test():
    scenario=sp.test_scenario()
    scenario.h1("Testing")
    jatin=sp.test_account("jatin")
    kumar=sp.test_account("kumar")
    
    store=Storage()
    scenario += store

    store.add(input("Enter your url")).run(sender=jatin)
    
            
                
            
            
            
            
            
                          
        
        
        
        
    