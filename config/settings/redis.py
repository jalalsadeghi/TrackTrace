from config.env import env


# Redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': env("REDIS_LOCATION", default="redis://localhost:6379"),
    }
}
# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15