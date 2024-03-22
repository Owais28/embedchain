from enum import Enum
import logging

logging.basicConfig(level=logging.DEBUG)

class ProgressStatus(Enum):
    ERROR = 'ERROR'
    SUCCESS = 'SUCCESS'
    IN_PROGRESS = 'IN_PROGRESS'

class Progress:
    progress: int
    result: ProgressStatus
    source: str
    
    def __init__(self, source: int):
        self.progress = 0
        self.result = ProgressStatus.IN_PROGRESS
        self.source = source

class Observer:
    def __init__(self, sources: list[str]):
        try:
            self.total = len(sources)
            self.progress_record = self._init_empty_progress_record(sources=sources)
            logging.info("Observer initiated: %s", self.progress_record)
        except Exception as e:
            print(f"Observer::__init__\nError: {e}")

    def update_progress(self, source: str, progress: int, total: int):
        try:
            percentage = (progress) / total * 100  # Calculate percentage
            self._update_property_in_list(source, 'progress', percentage)
            print(f'Update Progress >> Source {source}: {percentage}%')
        except Exception as e:
            print(f"Observer::update_progress\nError: {e}")

    def update_completed(self, source: str):
        try:
            self._update_property_in_list(source, 'result', ProgressStatus.SUCCESS.value)
            print(f'Update Complete >> Source {source}: {ProgressStatus.SUCCESS.value}')
        except Exception as e:
            print(f"Observer::update_completed\nError: {e}")

    def update_failed(self, source: str):
        try:
            self._update_property_in_list(source, 'result', ProgressStatus.ERROR.value)
            print(f'Update Fail >> Source {source}: {ProgressStatus.ERROR.value}')
        except Exception as e:
            print(f"Observer::update_failed\nError: {e}")

    def _init_empty_progress_record(self, sources: list[str]) -> list[dict]:
        try:
            initial_list = [{source : {'progress': 0,
                'result': ProgressStatus.IN_PROGRESS.value,
                'source': source}} for source in sources]
            # return [{source: {
            #     'progress': 0,
            #     'result': ProgressStatus.IN_PROGRESS.value,
            #     'source': source}} for source in sources]
            return initial_list
        except Exception as e:
            print(f"Observer::_init_empty_progress_record\nError: {e}")

    def _update_property_in_list(self, key_to_search, key_to_update, new_value):
        """
        Update a specific property in a dictionary within a list based on a search criteria.

        Args:
            value_to_search: The value to search for in the dictionaries.
            key_to_search (str): The key to search in dictionaries.
            key_to_update (str): The key of the property to update.
            new_value: The new value to assign to the property.
        """
        for item in self.progress_record:
            if item[key_to_search]:
                if key_to_update in item[key_to_search]:
                    item[key_to_search][key_to_update] = new_value
                else:
                    print(f"Key '{key_to_update}' not found in the dictionary.")
                break  # Exit loop after updating the first matching dictionary