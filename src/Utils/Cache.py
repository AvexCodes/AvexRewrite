from Utils.Logger import Logger

tiers_cache = {}
support_tickets_cache = {}
support_nums_id_cache = {}
ticket_numbers = []

logger = Logger(False)
class CacheManger:
    def clearcaches(self):
        tiers_cache = {}
        logger.warning("Cache Manager", "All caches reset!")

    def clearTiers(self):
        tiers_cache = {}
        logger.warning("Cache Manager", "Tier cache reset!")



def appendTiers(key: str=None, value=None):
    if key is None or value is None:
        return logger.error(name="Cache Manager", output="Not enough parameters passed!")
    
    tiers_cache[key] = value
    logger.log("Cache Manager", "Appended values to tier cache.")
    

