# GitHub Profile Analyzer API

A REST API built with Django and Django REST Framework that analyzes GitHub user profiles by integrating external API data and generating structured insights. The system processes repository data, extracts key metrics, and optimizes performance using database storage and Redis caching.


## Features

- Accepts a GitHub username via API endpoint
- Fetches user repository data from the GitHub API
- Implements error handling for invalid users and API failures
- Processes raw data to extract key insights:
  - Total repository count
  - Total stars across repositories
  - Most frequently used programming language
- Returns structured and clean JSON responses
- Stores processed results in PostgreSQL for reuse
- Uses database-first retrieval to avoid redundant external API calls
- Integrates Redis caching to further reduce repeated requests
- Updates cache on database hits to improve performance
- Reduces redundant GitHub API calls using layered caching (PostgreSQL + Redis)

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- Redis

## API Endpoint

### Analyze GitHub User

**GET** `/api/test/<username>/`

#### Description

Fetches GitHub data for the given username, processes repository information, and returns structured insights including repository count, total stars, and top language.


#### Example Request

``` 
http://127.0.0.1:8000/api/test/octocat/ 
```

#### Example Response

```json
{
    "Username": "octocat",
    "profile": {
        "name": "The Octocat",
        "public_repos": 8,
        "followers": 22439
    },
    "insights": {
        "top_language": "Ruby",
        "total_stars": 21268
    }
}