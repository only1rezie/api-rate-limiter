# API Rate Limiter Challenge

Implement a thread-safe, in-memory API rate limiter using the Token Bucket algorithm in Python.

### Requirements:
1. Parse a dynamic JSON log of inbound traffic containing client_id and timestamp.
2. Evaluate requests against a bucket limit of 5 tokens, refilling at a fractional rate of 1 token per second.
3. Output a sequential JSON array mapping each request payload directly to an HTTP status code (200 for allowed, 429 for rate-limited).
4. 
