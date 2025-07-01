from tarfile import data_filter

from django.core.cache import cache


class CacheMixin:
    def set_get_cache(self, query, cache_name, cache_time):
        cache_data = cache.get(cache_name)
        
        if not cache_data:
            cache_data = query
            cache.set(cache_name, cache_data, cache_time)
        
        return cache_data
    