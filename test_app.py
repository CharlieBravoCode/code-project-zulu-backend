
try:
    from app import app
    from app import Events
    import unittest 
    from unittest import mock
    import time
    from unittest.mock import patch, MagicMock

except Exception as e:
    print("Some Modules are Missing {}".format(e))

unittest.defaultTestLoader.sortTestMethodsUsing = lambda *args: -1


class FlaskTest(unittest.TestCase):
    

    # Check for Data returned in the response /events having: id, identifier, title, location, latitud, longitud
    def test_route_events_get_returns_correct_content(self):

        ### ARRANGE ###
        # Set test_client
        tester = app.test_client(self)

        ### ACT ###
        # Run test on route /events
        response = tester.get('/events')
        
        ### ASSERT ###
        # The response
        self.assertTrue(b'title' in response.data)
        self.assertTrue(b'identifier' in response.data)
        self.assertTrue(b'location' in response.data)
        self.assertTrue(b'latitud' in response.data)
        self.assertTrue(b'longitud' in response.data)
        self.assertTrue(b'id' in response.data)


    # Check for response 200 and 'Hello World!'
    def test_real_db_route_index_returns_200_and_HelloWorld(self):
        ### ARRANGE ###
        # Set test_client
        tester = app.test_client(self)

        ### ACT ###
        # Run test on route /
        response = tester.get('/')
        statuscode = response.status_code

        ### ASSERT ###
        self.assertEqual(statuscode, 200)
        self.assertTrue(b'Hello World' in response.data)

 

    # Check events get returns correct content with stub data   
    @mock.patch('app.Events')
    def test_real_db_route_events_get_returns_correct_content_with_mock_data(self, mock_event):
        ### ARRANGE ### 
        # Create test Events (db.model)
        test_event = Events()
        test_event.id = 1
        test_event.identifier = "test_identifier1"
        test_event.title = "test_title1"
        test_event.location = "test_location1"
        test_event.latitud = "1.1"
        test_event.longitud = "1.2"

        # Set return_value of all to list containing test event
        mock_event.query.all.return_value = [test_event]
        # Set test_client
        tester = app.test_client(self)

        ### ACT ### 
        # Run test on route /events              
        response = tester.get('/events')

        ### ASSERT ### 
        # Response content
        # --- Structure ---
        self.assertTrue(b'id' in response.data)
        self.assertTrue(b'identifier' in response.data)
        self.assertTrue(b'title' in response.data)
        self.assertTrue(b'location' in response.data)
        self.assertTrue(b'latitud' in response.data)
        self.assertTrue(b'longitud' in response.data)
        # --- Content ----
        self.assertTrue(b'1' in response.data)
        self.assertTrue(b'test_identifier1' in response.data)
        self.assertTrue(b'test_title1' in response.data)
        self.assertTrue(b'test_location1' in response.data)
        self.assertTrue(b'1.1' in response.data)
        self.assertTrue(b'1.2' in response.data)



    # Check if /events returns json return is application/json
    def test_real_db_route_events_returns_json(self):
        ### ARRANGE ###
        # Set test_client
        tester = app.test_client(self)

        ### ACT ###
        # Run test on route /events
        response = tester.get('/events')

        ### ASSERT ###
        # Check for json
        self.assertEqual(response.content_type, 'application/json')


    # Check for Data returned in the response '/events/geojson' 
    # is a geojson format
    def test_real_db_route_events_geojson_returns_geojson(self):
        # Set test_client
        tester = app.test_client(self)

        ### ACT ###
        # Run test on route /events/geojson
        response = tester.get('/events/geojson')

        ### ASSERT ###
        # Check for geojson attributes
        self.assertTrue(b'type' in response.data)
        self.assertTrue(b'features' in response.data)
        self.assertTrue(b'geometry' in response.data)
        self.assertTrue(b'properties' in response.data)


    
if __name__ == '__main__':
    unittest.main()