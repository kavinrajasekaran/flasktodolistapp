class Task():
    count = 1


    def __init__(self, event_name, event_description):
        self.event_name = event_name
        self.event_description = event_description
        self.id = Task.count
        Task.count += 1

        
