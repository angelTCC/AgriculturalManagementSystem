# **Crops API Documentation**

## **Base URL**
```
http://localhost:5000/api
```

### **POST /crops**
- **Description**: Adds a new crop to the system.
- **Request Body**:
  ```json
  {
    "field_id": 3,
    "crop_type": "rice",
    "planting_date": "2025-04-05",
    "harvest_date": "2025-07-20",
    "status": "planted"
  }
  ```
- **Response**:
  ```json
  {
    "crop_id": 6022,
    "message": "Crop registered successfully"
  }
  ```

### **Error Codes**
- `400 Bad Request`: Missing or invalid input.
- `500 Internal Server Error`: Server issue or database connection error.

---

This documentation focuses only on the functionality you've implemented (the `POST /crops` endpoint), keeping it concise and professional. You can update it with more details as you implement additional endpoints.