from typing import Dict, Any, Set, Optional


class CounterType:
    def __init__(self) -> None:
        # for each tag we create a reverse index
        self._indexes: Dict[str, Dict[Any, Set[Any]]] = dict()

    def put(self, *, tags: Dict[str, Any], item: Any) -> None:
        if not tags or "id" not in tags:
            raise Exception(
                "You need to pass in some tags, and the tags must contain "
                "at least the `id` key."
            )

        for tag_name, tag_value in tags.items():
            try:
                reverse_index = self._indexes[tag_name]
            except KeyError:
                reverse_index = dict()
                self._indexes[tag_name] = reverse_index

            try:
                set_items = reverse_index[tag_value]
            except KeyError:
                set_items = set()
                reverse_index[tag_value] = set_items

            set_items.add(item)

    def find(self, **kw) -> Optional[Set]:
        _it = kw.items().__iter__()

        tag_pair = _it.__next__()
        tag_name = tag_pair[0]
        tag_value = tag_pair[1]

        if tag_name not in self._indexes or \
                tag_value not in self._indexes[tag_name]:
            return None

        result_set = set(self._indexes[tag_name][tag_value])

        try:
            while result_set:
                tag_pair = _it.__next__()
                tag_name = tag_pair[0]
                tag_value = tag_pair[1]

                if tag_name not in self._indexes or \
                        tag_value not in self._indexes[tag_name]:
                    return None

                result_set.intersection_update(self._indexes[tag_name][tag_value])
        except StopIteration:
            pass

        return result_set
