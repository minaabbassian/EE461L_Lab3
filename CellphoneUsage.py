class CellphoneUsage:
    
    def __init__(self):
        #Define attributes
        self.minutes = 0
        self.texts = 0
        self.maxMins = 500
        self.maxTexts = 100
     
    def update_account_info(self, new_minutes, new_text):
        #This updates the new values for text and minutes to setup account info
        self.maxMins = new_minutes
        self.maxTexts = new_text
       
    def make_call(self, minutes):
        #This keeps track of how many minutes are used
        self.minutes += minutes
         
    def send_texts(self, texts):
        #This keeps track of how many texts are used
        self.texts += texts
        
    def view_current_usage(self):
        #This returns the total texts and minutes used
        return [self.minutes, self.texts]
        
    def finalize_bill(self):
        #This calculates the final bill and returns it
        final_cost = 79.95
        if self.minutes > self.maxMins:
            additional_mins = self.minutes - self.maxMins
            for x in range(additional_mins):
                final_cost += 0.25     
        
        if self.texts > self.maxTexts:
            additional_texts = self.texts - self.maxTexts
            for x in range(additional_texts):
                final_cost += 0.20 
        return (final_cost)
