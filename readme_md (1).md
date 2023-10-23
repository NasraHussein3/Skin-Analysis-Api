# Skin Care Analysis API

## Introduction

Welcome to the Skin Analysis API – your personal skincare companion, offering customized regimens tailored to your unique skin type. We base our recommendations on The Ordinary skincare products to help you achieve healthy and radiant skin.

In the development of this API, we used the following tools:

1. **Flask Web Framework:** We've implemented Flask, a web framework, to create the web application.

2. **Jsonify:** This library enables us to provide JSON responses, making it easy for users to understand and work with the data.

3. **Request:** The Request library allows us to handle incoming data, such as the JSON input provided by users.

## Endpoints

This API simplifies your skincare journey with four comprehensive endpoints:

### 1. Explore Available Skincare Data

- Endpoint: `/skincare`
- Description: Explore a dataset of skincare information, including detailed skincare routines and product recommendations. The information is tailored to specific skin types, which include:
  - Oily skin
  - Dry skin
  - Combination skin
  - Normal skin
  - Ageing skin
  - Acne-prone skin
  This endpoint offers insights into The Ordinary products.

### 2. Discover Your Ideal Routine

- Endpoint: `/skincare_routine`
- Description: Select your skin type from the following options:
  - Oily skin
  - Dry skin
  - Combination skin
  - Normal skin
  - Ageing skin
  - Acne-prone skin
  The API will provide a detailed skincare regimen, including cleansing, toning, serums, moisturizers, and UV protection, using premier products from The Ordinary.

### 3. List Available Skin Types

- Endpoint: `/skin_types`
- Description: View a comprehensive list of available skin types. This feature provides a reference to help you choose the skin type that best matches your needs, ensuring an accurate and tailored skincare routine.

### 4. Reset and Start Anew

- Endpoint: `/skincare_data`
- Description: Use this endpoint as a reset button to wipe out all existing skincare data. The API responds with a reassuring message: "All skincare data has been deleted."

Feel free to utilize this API to enhance your skincare routine and achieve beautiful, healthy skin!

## Get Started

To get started, check out the API documentation for each endpoint and enjoy a personalized skincare experience.
