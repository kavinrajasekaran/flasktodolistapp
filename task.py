class Task():
    count = 1


    def __init__(self, event_name, event_description, event_date):
        self.event_name = event_name
        self.event_description = event_description
        self.event_date = event_date
        self.id = Task.count
        Task.count += 1
