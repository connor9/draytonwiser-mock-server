class WiserBaseAPI(object):
        
    def __init__(self):
        pass

    def _get_item_if_exists(self, item, data):
        """Retrieves the JSON object for a specific ID of a /data/domain/[item]/[id] call"""

        item_id = item[item.index('/') + 1:]
        if len(item_id) > 0 and item_id is not None:
            # we have an id
            item_id = int(item_id)
            found = False
            if item_id >= 0:
                for temp_item in data:
                    if temp_item['id'] == item_id:
                        data = temp_item
                        found = True
                        break
            if not found:
                raise ObjectNotFoundException("Item ID not found")

        return data
        
    def _parse_item_data(self, item, data):
        """Parses data from /data/domain/ call to serve it as if /data/domain/[Item]/[ID] was called

            This has been added to provide compatibility for the library supporting direct restful
            calls to specific endpoints. At the moment each call gets the root /data/domain/ for caching
                but may be split out into separate calls when caching is made more robust.
        """

        if item.startswith('HeatingChannel'):
            data = self._get_item_if_exists(item, data['HeatingChannel'])
        elif item.startswith('HotWater'):
            data = self._get_item_if_exists(item, data['HotWater'])
        elif item.startswith('Device'):
            data = self._get_item_if_exists(item, data['Device'])
        elif item.startswith('RoomStat'):
            data = self._get_item_if_exists(item, data['RoomStat'])
        elif item.startswith('Room'):
            data = self._get_item_if_exists(item, data['Room'])
        elif item.startswith('Cloud'):
            data = data['Cloud']
        elif item.startswith('System'):
            data = data['System']
        elif item.startswith('SmartValve'):
            data = self._get_item_if_exists(item, data['SmartValve'])
        elif item.startswith('Schedule'):
            data = self._get_item_if_exists(item, data['Schedule'])

        return data