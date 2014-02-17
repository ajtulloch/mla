import json
import logging
import pdb
log = logging.getLogger(__name__)

EXAMPLE_TABLE_NAME = 'requests'


class Storage(object):
    def __init__(self, db):
        """
        """
        self._db = db

    def add(self, train_request):
        row = {
            'features': json.dumps(list(train_request.features)),
            'label': train_request.label
        }
        log.info(row)
        self._db[EXAMPLE_TABLE_NAME].insert(row, ensure=True)

    def samples(self):
        def deserialize(row):
            return {
                'label': bool(row['label']),
                'features': json.loads(row['features']),
            }

        return (deserialize(row)
                for row in self._db[EXAMPLE_TABLE_NAME].all())
