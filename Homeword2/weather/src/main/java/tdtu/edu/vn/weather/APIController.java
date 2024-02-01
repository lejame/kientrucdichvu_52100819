package tdtu.edu.vn.weather;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.Mapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/weather")
public class APIController {
    public String key = "0c55a4ae0f482cddb728a06b09cd581f";

    @GetMapping("/hello")
    public ResponseEntity<?> response() {
        // Replace the hardcoded coordinates with your actual data if needed
        double latitude = 44.34;
        double longitude = 10.99;

        // Build the API URL
        String apiUrl = "https://api.openweathermap.org/data/2.5/weather?lat=" + latitude + "&lon=" + longitude + "&appid=" + key;

        // Use RestTemplate to make a GET request to the API
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> apiResponse = restTemplate.getForEntity(apiUrl, String.class);

        // Check if the request was successful (HTTP status code 200)
        if (apiResponse.getStatusCode() == HttpStatus.OK) {
            // Return the API response body (JSON) as is
            return new ResponseEntity<>(apiResponse.getBody(), HttpStatus.OK);
        } else {
            // If the request was not successful, return an error response
            return new ResponseEntity<>("Failed to fetch weather data", HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
