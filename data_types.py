class Purchase:
    def __init__(self, street,city,zip,state,beds,baths,sq__ft,home_type,sale_date,price,latitude,longitude):
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sq__ft = sq__ft
        self.type = home_type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude


    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            lookup['street'],
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            int(lookup['sq__ft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['longitude'])
        )
